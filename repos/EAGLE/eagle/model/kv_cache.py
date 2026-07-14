import torch


class PastKeyValueSegment:
    """
    Wrapper for a segment tensor that allows dynamic resizing of the time dimension.
    Acts like a tensor for indexing (`__getitem__`) and forwards common attrs.
    """
    def __init__(self, tensor: torch.Tensor):
        self.tensor = tensor

    def ensure_capacity(self, required_len: int, margin: int = 16):
        # time dimension is at index 3 for the full segment tensor
        old_len = self.tensor.shape[3]
        if required_len <= old_len:
            return
        # geometric growth: 1.5x or required + margin, whichever larger
        new_len = max(int(old_len * 1.5), required_len + margin)
        shape = list(self.tensor.shape)
        shape[3] = new_len
        new_tensor = torch.zeros(*shape, device=self.tensor.device, dtype=self.tensor.dtype)
        # copy existing contents
        new_tensor[..., :old_len, :] = self.tensor
        self.tensor = new_tensor

    def __getitem__(self, item):
        return self.tensor[item]

    def __getattr__(self, name):
        # forward attributes to the underlying tensor when possible
        try:
            return getattr(self.tensor, name)
        except Exception:
            raise AttributeError(name)


class KVCache:
    """
    A key-value cache for the model.

    This class provides a mechanism to maintain a growing cache of keys and values,
    particularly useful for models that benefit from caching previous states,
    like transformers during autoregressive decoding.

    Attributes:
        data (torch.Tensor): The tensor storing keys and values.
        current_length (int): Current length of the data being stored.
    """

    def __init__(self, data, current_length):
        """
        Initialize the KVCache.

        Args:
            data (torch.Tensor or PastKeyValueSegment view): Initial tensor view or
                a slice view created from a `PastKeyValueSegment` via indexing.
            current_length (torch.Tensor): Tensor tracking current length for this cache.
        """
        # `data` may be either:
        # - a tuple (PastKeyValueSegment, index) indicating which slice to use
        # - a plain tensor view (legacy)
        if isinstance(data, tuple) or isinstance(data, list):
            seg, idx = data
            self._segment = seg
            self._index = int(idx)
            self._data_view = None
        else:
            self._segment = None
            self._index = None
            self._data_view = data
        self.current_length = current_length

    @property
    def shape(self):
        """Return the shape of the data tensor with updated length."""
        v = self._get_view()
        return (v.shape[0], v.shape[1], self.current_length.item(), v.shape[3])

    def _get_view(self):
        """Return the current tensor view for this cache (fresh after resizes)."""
        if self._segment is not None:
            return self._segment.tensor[self._index]
        return self._data_view

    def copy(self, indices: torch.Tensor, prev_length: int, dim: int = 2):
        """
        Copy values from the current data at specified indices to a new location.

        Args:
            indices (torch.Tensor): Indices of the data tensor to be copied.
            prev_length (int): Previous length before adding new data.
            dim (int, optional): Dimension along which copying should be performed. Default is 2.
        """
        # operate on the current view
        view = self._get_view()
        tgt = view.index_select(dim, indices)
        dst = view.narrow(dim, prev_length, tgt.shape[dim])
        dst.copy_(tgt, non_blocking=True)
        self.current_length.fill_(prev_length + tgt.shape[dim])

    def cat(self, tensor: torch.Tensor, dim: int = 2):
        """
        Concatenate the given tensor with the current data.

        Args:
            tensor (torch.Tensor): The tensor to be concatenated.
            dim (int, optional): The dimension along which concatenation should be done. Default is 2.

        Returns:
            torch.Tensor: The data tensor after concatenation up to the current length.
        """
        # Ensure the underlying storage has enough capacity. The view's time
        # dimension is at index `dim` in the view; for the full segment tensor,
        # that corresponds to index 3. If the view is a slice of a segment,
        # call ensure_capacity on the parent segment.
        view = self._data_view
        # Calculate required length
        req = int(self.current_length.item()) + int(tensor.shape[dim])
        # If backed by a PastKeyValueSegment, ensure its capacity first so any
        # view slices we take will reflect the new storage.
        if self._segment is not None:
            try:
                self._segment.ensure_capacity(req)
            except Exception:
                pass
            view = self._get_view()
        else:
            base = getattr(view, "_base", None)
            # view is a view of another tensor
            if base is not None and hasattr(base, 'shape'):
                try:
                    old_len = view.shape[dim]
                    if req > old_len:
                        # allocate a larger tensor for the view shape
                        shape = list(view.shape)
                        new_len = max(int(old_len * 1.5), req + 16)
                        shape[dim] = new_len
                        new_view = torch.zeros(*shape, device=view.device, dtype=view.dtype)
                        new_view[..., :old_len, :] = view
                        # update our view reference
                        self._data_view = new_view
                        view = self._data_view
                except Exception:
                    pass
            else:
                # view is standalone tensor, ensure capacity by reallocating
                old_len = view.shape[dim]
                if req > old_len:
                    shape = list(view.shape)
                    new_len = max(int(old_len * 1.5), req + 16)
                    shape[dim] = new_len
                    new_view = torch.zeros(*shape, device=view.device, dtype=view.dtype)
                    new_view[..., :old_len, :] = view
                    self._data_view = new_view
                    view = self._data_view

        dst = view.narrow(dim, int(self.current_length.item()), tensor.shape[dim])
        dst.copy_(tensor)
        self.current_length.add_(tensor.shape[dim])
        return torch.narrow(view, 2, 0, int(self.current_length.item()))


def initialize_past_key_values(model,max_length=2200):
    """
    Initialize past key and value states for a given transformer model.

    This function prepares key-value cache structures for the model, allowing it to store and reuse
    past key and value states during autoregressive decoding, which can improve efficiency.

    Args:
        model (nn.Module): The transformer model for which past key-value states need to be initialized.

    Returns:
        tuple:
            - past_key_values (list): A list of KVCache objects for each layer in the model.
            - past_key_values_data (torch.Tensor): The tensor that will store all keys and values.
            - current_length_data (torch.Tensor): A tensor tracking the current length of keys/values in the cache.
    """
    # Extracting configuration from the model
    config = model.config
    # Initializing the batch size to 1, this can be modified if different batch sizes are required
    batch_size = 1
    # Initializing a tensor to store past keys and values for all layers

    devices=[]
    for i in range(config.num_hidden_layers):
        try:
            device = model.model.layers[i].self_attn.q_proj.weight.device
        except:
            device=model.layers[i].self_attn.q_proj.weight.device
        devices.append(device)
    past_key_values_data_list = []
    segment_id_by_layer = []
    layers_per_segment = []

    startnum = 0
    startdevice = devices[0]
    current_segment_id = 0
    for i in devices:
        if startdevice != i:
            past_key_values_data = torch.zeros(
                startnum * 2,
                batch_size,
                config.num_key_value_heads,
                max_length,
                getattr(config, "head_dim", config.hidden_size // config.num_attention_heads),
                device=startdevice,
                dtype=model.dtype,
            )
            # wrap in a PastKeyValueSegment for dynamic resizing
            past_key_values_data_list.append(PastKeyValueSegment(past_key_values_data))
            layers_per_segment.append(startnum)
            current_segment_id += 1
            startdevice = i
            startnum = 0
        segment_id_by_layer.append(current_segment_id)
        startnum += 1

    past_key_values_data = torch.zeros(
        startnum * 2,
        batch_size,
        config.num_key_value_heads,
        max_length,
        getattr(config, "head_dim", config.hidden_size // config.num_attention_heads),
        device=startdevice,
        dtype=model.dtype,
    )
    past_key_values_data_list.append(PastKeyValueSegment(past_key_values_data))
    layers_per_segment.append(startnum)
    # Initialize tensor to store the current length of the cached data for all layers.
    # [IMPORTANT] It needs to be kept on CPU for quick access and updates.
    current_length_data = torch.zeros(
        config.num_hidden_layers * 2, dtype=torch.long, device="cpu"
    )
    # Creating a KVCache for each pair of key and value in all layers
    past_key_values = [] * config.num_hidden_layers

    layer_offset_in_segment = [0 for _ in range(len(past_key_values_data_list))]
    for i in range(config.num_hidden_layers):
        seg_id = segment_id_by_layer[i]
        bias = layer_offset_in_segment[seg_id]
        past_key_values.append(
            [
                KVCache(
                    (past_key_values_data_list[seg_id], 2 * bias + j),
                    current_length_data[i * 2 + j],
                )
                for j in range(2)
            ]
        )
        layer_offset_in_segment[seg_id] += 1
    return past_key_values, past_key_values_data_list, current_length_data
