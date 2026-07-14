import torch
from eagle.model.kv_cache import PastKeyValueSegment, KVCache


def test_kvcache_resize_and_copy():
    # create a small segment: (segments, batch, heads, time, head_dim)
    seg_tensor = torch.zeros((2, 1, 2, 4, 8))
    segment = PastKeyValueSegment(seg_tensor)

    # current length scalar tensor
    current_length = torch.tensor(0, dtype=torch.long)

    # create KVCache for segment index 0
    kv = KVCache((segment, 0), current_length)

    # create data to concatenate: (batch, heads, new_time, head_dim)
    new_time = 3
    data = torch.arange(1, 1 + 1 * 2 * new_time * 8, dtype=torch.float32).view(1, 2, new_time, 8)

    # call cat which should trigger resize if needed and copy data
    out = kv.cat(data)

    assert current_length.item() == new_time
    # verify that the underlying segment received the data at the start
    view = segment.tensor[0]
    copied = view[:, :, :new_time, :]
    assert torch.allclose(copied, data)
    # returned tensor shape should match current length
    assert out.shape[2] == new_time


def test_kvcache_resize_trigger():
    # force a resize by concatenating more time steps than initial capacity
    seg_tensor = torch.zeros((1, 1, 1, 4, 8))
    segment = PastKeyValueSegment(seg_tensor)
    current_length = torch.tensor(0, dtype=torch.long)
    kv = KVCache((segment, 0), current_length)

    new_time = 6
    data = torch.arange(1, 1 + 1 * 1 * new_time * 8, dtype=torch.float32).view(1, 1, new_time, 8)
    out = kv.cat(data)
    assert current_length.item() == new_time
    view = segment.tensor[0]
    copied = view[:, :, :new_time, :]
    assert torch.allclose(copied, data)
    assert out.shape[2] == new_time
