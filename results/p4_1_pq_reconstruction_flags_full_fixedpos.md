# P4.1 pq Reconstruction Flags

Tolerance: 1e-06
Total rows processed: 236235
Invalid rows: 961
Invalid %: 0.406798%

Root cause note: unresolved (execution-path numerical drift vs context/state reconstruction mismatch).
Policy note: flagged rows are excluded from confirmatory P4.1 statistics and are not corrected/substituted.

## Breakdown by Dataset
- livecodebench: rows=100252, invalid=411, invalid_pct=0.409967%
- math500: rows=135983, invalid=550, invalid_pct=0.404462%

## Breakdown by Row Type
- post_rejection: rows=81879, invalid=326, invalid_pct=0.398148%
- normal: rows=154356, invalid=635, invalid_pct=0.411387%

## Breakdown by Position
- position=0: rows=350, invalid=0, invalid_pct=0.000000%
- position=1: rows=350, invalid=6, invalid_pct=1.714286%
- position=2: rows=350, invalid=2, invalid_pct=0.571429%
- position=3: rows=350, invalid=2, invalid_pct=0.571429%
- position=4: rows=350, invalid=0, invalid_pct=0.000000%
- position=5: rows=350, invalid=2, invalid_pct=0.571429%
- position=6: rows=350, invalid=2, invalid_pct=0.571429%
- position=7: rows=350, invalid=0, invalid_pct=0.000000%
- position=8: rows=350, invalid=1, invalid_pct=0.285714%
- position=9: rows=350, invalid=1, invalid_pct=0.285714%
- position=10: rows=350, invalid=2, invalid_pct=0.571429%
- position=11: rows=350, invalid=2, invalid_pct=0.571429%
- position=12: rows=350, invalid=1, invalid_pct=0.285714%
- position=13: rows=350, invalid=1, invalid_pct=0.285714%
- position=14: rows=350, invalid=3, invalid_pct=0.857143%
- position=15: rows=350, invalid=2, invalid_pct=0.571429%
- position=16: rows=350, invalid=1, invalid_pct=0.285714%
- position=17: rows=350, invalid=2, invalid_pct=0.571429%
- position=18: rows=350, invalid=3, invalid_pct=0.857143%
- position=19: rows=350, invalid=0, invalid_pct=0.000000%
- position=20: rows=350, invalid=0, invalid_pct=0.000000%
- position=21: rows=350, invalid=3, invalid_pct=0.857143%
- position=22: rows=350, invalid=2, invalid_pct=0.571429%
- position=23: rows=350, invalid=1, invalid_pct=0.285714%
- position=24: rows=350, invalid=0, invalid_pct=0.000000%
- position=25: rows=350, invalid=3, invalid_pct=0.857143%
- position=26: rows=350, invalid=2, invalid_pct=0.571429%
- position=27: rows=350, invalid=0, invalid_pct=0.000000%
- position=28: rows=350, invalid=0, invalid_pct=0.000000%
- position=29: rows=350, invalid=3, invalid_pct=0.857143%
- position=30: rows=350, invalid=2, invalid_pct=0.571429%
- position=31: rows=350, invalid=4, invalid_pct=1.142857%
- position=32: rows=350, invalid=4, invalid_pct=1.142857%
- position=33: rows=350, invalid=2, invalid_pct=0.571429%
- position=34: rows=350, invalid=1, invalid_pct=0.285714%
- position=35: rows=350, invalid=3, invalid_pct=0.857143%
- position=36: rows=350, invalid=1, invalid_pct=0.285714%
- position=37: rows=350, invalid=1, invalid_pct=0.285714%
- position=38: rows=350, invalid=3, invalid_pct=0.857143%
- position=39: rows=350, invalid=1, invalid_pct=0.285714%
- position=40: rows=350, invalid=3, invalid_pct=0.857143%
- position=41: rows=350, invalid=1, invalid_pct=0.285714%
- position=42: rows=350, invalid=1, invalid_pct=0.285714%
- position=43: rows=350, invalid=1, invalid_pct=0.285714%
- position=44: rows=350, invalid=0, invalid_pct=0.000000%
- position=45: rows=350, invalid=2, invalid_pct=0.571429%
- position=46: rows=350, invalid=2, invalid_pct=0.571429%
- position=47: rows=350, invalid=2, invalid_pct=0.571429%
- position=48: rows=350, invalid=1, invalid_pct=0.285714%
- position=49: rows=350, invalid=0, invalid_pct=0.000000%
- position=50: rows=350, invalid=0, invalid_pct=0.000000%
- position=51: rows=350, invalid=5, invalid_pct=1.428571%
- position=52: rows=350, invalid=0, invalid_pct=0.000000%
- position=53: rows=350, invalid=1, invalid_pct=0.285714%
- position=54: rows=350, invalid=5, invalid_pct=1.428571%
- position=55: rows=350, invalid=2, invalid_pct=0.571429%
- position=56: rows=350, invalid=1, invalid_pct=0.285714%
- position=57: rows=350, invalid=1, invalid_pct=0.285714%
- position=58: rows=350, invalid=3, invalid_pct=0.857143%
- position=59: rows=350, invalid=3, invalid_pct=0.857143%
- position=60: rows=350, invalid=2, invalid_pct=0.571429%
- position=61: rows=350, invalid=2, invalid_pct=0.571429%
- position=62: rows=350, invalid=2, invalid_pct=0.571429%
- position=63: rows=350, invalid=2, invalid_pct=0.571429%
- position=64: rows=350, invalid=2, invalid_pct=0.571429%
- position=65: rows=350, invalid=0, invalid_pct=0.000000%
- position=66: rows=350, invalid=0, invalid_pct=0.000000%
- position=67: rows=350, invalid=1, invalid_pct=0.285714%
- position=68: rows=350, invalid=4, invalid_pct=1.142857%
- position=69: rows=350, invalid=0, invalid_pct=0.000000%
- position=70: rows=350, invalid=0, invalid_pct=0.000000%
- position=71: rows=350, invalid=0, invalid_pct=0.000000%
- position=72: rows=350, invalid=0, invalid_pct=0.000000%
- position=73: rows=350, invalid=3, invalid_pct=0.857143%
- position=74: rows=350, invalid=1, invalid_pct=0.285714%
- position=75: rows=350, invalid=2, invalid_pct=0.571429%
- position=76: rows=350, invalid=1, invalid_pct=0.285714%
- position=77: rows=350, invalid=0, invalid_pct=0.000000%
- position=78: rows=350, invalid=0, invalid_pct=0.000000%
- position=79: rows=350, invalid=1, invalid_pct=0.285714%
- position=80: rows=350, invalid=0, invalid_pct=0.000000%
- position=81: rows=350, invalid=0, invalid_pct=0.000000%
- position=82: rows=350, invalid=0, invalid_pct=0.000000%
- position=83: rows=350, invalid=2, invalid_pct=0.571429%
- position=84: rows=350, invalid=1, invalid_pct=0.285714%
- position=85: rows=350, invalid=0, invalid_pct=0.000000%
- position=86: rows=350, invalid=2, invalid_pct=0.571429%
- position=87: rows=350, invalid=1, invalid_pct=0.285714%
- position=88: rows=350, invalid=2, invalid_pct=0.571429%
- position=89: rows=350, invalid=1, invalid_pct=0.285714%
- position=90: rows=350, invalid=1, invalid_pct=0.285714%
- position=91: rows=350, invalid=0, invalid_pct=0.000000%
- position=92: rows=350, invalid=5, invalid_pct=1.428571%
- position=93: rows=350, invalid=1, invalid_pct=0.285714%
- position=94: rows=350, invalid=0, invalid_pct=0.000000%
- position=95: rows=350, invalid=3, invalid_pct=0.857143%
- position=96: rows=350, invalid=2, invalid_pct=0.571429%
- position=97: rows=350, invalid=2, invalid_pct=0.571429%
- position=98: rows=350, invalid=1, invalid_pct=0.285714%
- position=99: rows=350, invalid=3, invalid_pct=0.857143%
- position=100: rows=350, invalid=0, invalid_pct=0.000000%
- position=101: rows=350, invalid=2, invalid_pct=0.571429%
- position=102: rows=350, invalid=1, invalid_pct=0.285714%
- position=103: rows=350, invalid=0, invalid_pct=0.000000%
- position=104: rows=350, invalid=0, invalid_pct=0.000000%
- position=105: rows=350, invalid=2, invalid_pct=0.571429%
- position=106: rows=350, invalid=1, invalid_pct=0.285714%
- position=107: rows=350, invalid=2, invalid_pct=0.571429%
- position=108: rows=350, invalid=3, invalid_pct=0.857143%
- position=109: rows=350, invalid=0, invalid_pct=0.000000%
- position=110: rows=350, invalid=0, invalid_pct=0.000000%
- position=111: rows=350, invalid=1, invalid_pct=0.285714%
- position=112: rows=350, invalid=0, invalid_pct=0.000000%
- position=113: rows=350, invalid=4, invalid_pct=1.142857%
- position=114: rows=350, invalid=2, invalid_pct=0.571429%
- position=115: rows=350, invalid=1, invalid_pct=0.285714%
- position=116: rows=350, invalid=0, invalid_pct=0.000000%
- position=117: rows=350, invalid=1, invalid_pct=0.285714%
- position=118: rows=350, invalid=4, invalid_pct=1.142857%
- position=119: rows=350, invalid=0, invalid_pct=0.000000%
- position=120: rows=350, invalid=3, invalid_pct=0.857143%
- position=121: rows=350, invalid=1, invalid_pct=0.285714%
- position=122: rows=350, invalid=1, invalid_pct=0.285714%
- position=123: rows=350, invalid=4, invalid_pct=1.142857%
- position=124: rows=350, invalid=2, invalid_pct=0.571429%
- position=125: rows=350, invalid=3, invalid_pct=0.857143%
- position=126: rows=350, invalid=1, invalid_pct=0.285714%
- position=127: rows=350, invalid=1, invalid_pct=0.285714%
- position=128: rows=350, invalid=2, invalid_pct=0.571429%
- position=129: rows=350, invalid=3, invalid_pct=0.857143%
- position=130: rows=350, invalid=2, invalid_pct=0.571429%
- position=131: rows=349, invalid=1, invalid_pct=0.286533%
- position=132: rows=349, invalid=0, invalid_pct=0.000000%
- position=133: rows=349, invalid=1, invalid_pct=0.286533%
- position=134: rows=349, invalid=1, invalid_pct=0.286533%
- position=135: rows=349, invalid=0, invalid_pct=0.000000%
- position=136: rows=349, invalid=0, invalid_pct=0.000000%
- position=137: rows=349, invalid=1, invalid_pct=0.286533%
- position=138: rows=349, invalid=2, invalid_pct=0.573066%
- position=139: rows=349, invalid=0, invalid_pct=0.000000%
- position=140: rows=349, invalid=3, invalid_pct=0.859599%
- position=141: rows=349, invalid=2, invalid_pct=0.573066%
- position=142: rows=349, invalid=1, invalid_pct=0.286533%
- position=143: rows=349, invalid=0, invalid_pct=0.000000%
- position=144: rows=349, invalid=3, invalid_pct=0.859599%
- position=145: rows=349, invalid=0, invalid_pct=0.000000%
- position=146: rows=349, invalid=2, invalid_pct=0.573066%
- position=147: rows=349, invalid=0, invalid_pct=0.000000%
- position=148: rows=349, invalid=0, invalid_pct=0.000000%
- position=149: rows=349, invalid=2, invalid_pct=0.573066%
- position=150: rows=349, invalid=0, invalid_pct=0.000000%
- position=151: rows=349, invalid=2, invalid_pct=0.573066%
- position=152: rows=349, invalid=2, invalid_pct=0.573066%
- position=153: rows=348, invalid=0, invalid_pct=0.000000%
- position=154: rows=348, invalid=1, invalid_pct=0.287356%
- position=155: rows=348, invalid=0, invalid_pct=0.000000%
- position=156: rows=348, invalid=4, invalid_pct=1.149425%
- position=157: rows=348, invalid=3, invalid_pct=0.862069%
- position=158: rows=348, invalid=1, invalid_pct=0.287356%
- position=159: rows=348, invalid=1, invalid_pct=0.287356%
- position=160: rows=348, invalid=2, invalid_pct=0.574713%
- position=161: rows=348, invalid=0, invalid_pct=0.000000%
- position=162: rows=348, invalid=1, invalid_pct=0.287356%
- position=163: rows=348, invalid=2, invalid_pct=0.574713%
- position=164: rows=348, invalid=2, invalid_pct=0.574713%
- position=165: rows=348, invalid=4, invalid_pct=1.149425%
- position=166: rows=348, invalid=0, invalid_pct=0.000000%
- position=167: rows=348, invalid=2, invalid_pct=0.574713%
- position=168: rows=348, invalid=1, invalid_pct=0.287356%
- position=169: rows=348, invalid=2, invalid_pct=0.574713%
- position=170: rows=348, invalid=1, invalid_pct=0.287356%
- position=171: rows=347, invalid=2, invalid_pct=0.576369%
- position=172: rows=347, invalid=2, invalid_pct=0.576369%
- position=173: rows=347, invalid=0, invalid_pct=0.000000%
- position=174: rows=347, invalid=2, invalid_pct=0.576369%
- position=175: rows=347, invalid=3, invalid_pct=0.864553%
- position=176: rows=347, invalid=0, invalid_pct=0.000000%
- position=177: rows=347, invalid=0, invalid_pct=0.000000%
- position=178: rows=347, invalid=0, invalid_pct=0.000000%
- position=179: rows=347, invalid=1, invalid_pct=0.288184%
- position=180: rows=347, invalid=1, invalid_pct=0.288184%
- position=181: rows=347, invalid=2, invalid_pct=0.576369%
- position=182: rows=347, invalid=1, invalid_pct=0.288184%
- position=183: rows=347, invalid=1, invalid_pct=0.288184%
- position=184: rows=345, invalid=3, invalid_pct=0.869565%
- position=185: rows=345, invalid=0, invalid_pct=0.000000%
- position=186: rows=344, invalid=1, invalid_pct=0.290698%
- position=187: rows=344, invalid=1, invalid_pct=0.290698%
- position=188: rows=344, invalid=2, invalid_pct=0.581395%
- position=189: rows=344, invalid=3, invalid_pct=0.872093%
- position=190: rows=344, invalid=2, invalid_pct=0.581395%
- position=191: rows=344, invalid=1, invalid_pct=0.290698%
- position=192: rows=344, invalid=1, invalid_pct=0.290698%
- position=193: rows=344, invalid=2, invalid_pct=0.581395%
- position=194: rows=344, invalid=0, invalid_pct=0.000000%
- position=195: rows=344, invalid=4, invalid_pct=1.162791%
- position=196: rows=344, invalid=1, invalid_pct=0.290698%
- position=197: rows=344, invalid=1, invalid_pct=0.290698%
- position=198: rows=344, invalid=1, invalid_pct=0.290698%
- position=199: rows=344, invalid=4, invalid_pct=1.162791%
- position=200: rows=343, invalid=0, invalid_pct=0.000000%
- position=201: rows=343, invalid=3, invalid_pct=0.874636%
- position=202: rows=343, invalid=2, invalid_pct=0.583090%
- position=203: rows=343, invalid=0, invalid_pct=0.000000%
- position=204: rows=343, invalid=1, invalid_pct=0.291545%
- position=205: rows=343, invalid=1, invalid_pct=0.291545%
- position=206: rows=343, invalid=2, invalid_pct=0.583090%
- position=207: rows=343, invalid=2, invalid_pct=0.583090%
- position=208: rows=343, invalid=2, invalid_pct=0.583090%
- position=209: rows=343, invalid=1, invalid_pct=0.291545%
- position=210: rows=343, invalid=0, invalid_pct=0.000000%
- position=211: rows=343, invalid=4, invalid_pct=1.166181%
- position=212: rows=343, invalid=2, invalid_pct=0.583090%
- position=213: rows=343, invalid=3, invalid_pct=0.874636%
- position=214: rows=343, invalid=0, invalid_pct=0.000000%
- position=215: rows=343, invalid=2, invalid_pct=0.583090%
- position=216: rows=343, invalid=3, invalid_pct=0.874636%
- position=217: rows=343, invalid=5, invalid_pct=1.457726%
- position=218: rows=343, invalid=1, invalid_pct=0.291545%
- position=219: rows=343, invalid=0, invalid_pct=0.000000%
- position=220: rows=343, invalid=1, invalid_pct=0.291545%
- position=221: rows=343, invalid=2, invalid_pct=0.583090%
- position=222: rows=343, invalid=1, invalid_pct=0.291545%
- position=223: rows=343, invalid=1, invalid_pct=0.291545%
- position=224: rows=343, invalid=1, invalid_pct=0.291545%
- position=225: rows=343, invalid=3, invalid_pct=0.874636%
- position=226: rows=343, invalid=2, invalid_pct=0.583090%
- position=227: rows=342, invalid=0, invalid_pct=0.000000%
- position=228: rows=342, invalid=0, invalid_pct=0.000000%
- position=229: rows=342, invalid=2, invalid_pct=0.584795%
- position=230: rows=342, invalid=1, invalid_pct=0.292398%
- position=231: rows=342, invalid=0, invalid_pct=0.000000%
- position=232: rows=342, invalid=1, invalid_pct=0.292398%
- position=233: rows=342, invalid=1, invalid_pct=0.292398%
- position=234: rows=342, invalid=2, invalid_pct=0.584795%
- position=235: rows=341, invalid=2, invalid_pct=0.586510%
- position=236: rows=341, invalid=0, invalid_pct=0.000000%
- position=237: rows=340, invalid=2, invalid_pct=0.588235%
- position=238: rows=339, invalid=0, invalid_pct=0.000000%
- position=239: rows=339, invalid=1, invalid_pct=0.294985%
- position=240: rows=339, invalid=3, invalid_pct=0.884956%
- position=241: rows=339, invalid=2, invalid_pct=0.589971%
- position=242: rows=339, invalid=0, invalid_pct=0.000000%
- position=243: rows=339, invalid=1, invalid_pct=0.294985%
- position=244: rows=339, invalid=1, invalid_pct=0.294985%
- position=245: rows=339, invalid=1, invalid_pct=0.294985%
- position=246: rows=339, invalid=0, invalid_pct=0.000000%
- position=247: rows=339, invalid=2, invalid_pct=0.589971%
- position=248: rows=339, invalid=5, invalid_pct=1.474926%
- position=249: rows=339, invalid=2, invalid_pct=0.589971%
- position=250: rows=339, invalid=2, invalid_pct=0.589971%
- position=251: rows=339, invalid=0, invalid_pct=0.000000%
- position=252: rows=338, invalid=3, invalid_pct=0.887574%
- position=253: rows=338, invalid=1, invalid_pct=0.295858%
- position=254: rows=338, invalid=2, invalid_pct=0.591716%
- position=255: rows=338, invalid=0, invalid_pct=0.000000%
- position=256: rows=338, invalid=1, invalid_pct=0.295858%
- position=257: rows=338, invalid=0, invalid_pct=0.000000%
- position=258: rows=338, invalid=1, invalid_pct=0.295858%
- position=259: rows=338, invalid=0, invalid_pct=0.000000%
- position=260: rows=338, invalid=0, invalid_pct=0.000000%
- position=261: rows=338, invalid=1, invalid_pct=0.295858%
- position=262: rows=338, invalid=0, invalid_pct=0.000000%
- position=263: rows=338, invalid=1, invalid_pct=0.295858%
- position=264: rows=338, invalid=2, invalid_pct=0.591716%
- position=265: rows=338, invalid=0, invalid_pct=0.000000%
- position=266: rows=338, invalid=1, invalid_pct=0.295858%
- position=267: rows=338, invalid=2, invalid_pct=0.591716%
- position=268: rows=338, invalid=1, invalid_pct=0.295858%
- position=269: rows=338, invalid=1, invalid_pct=0.295858%
- position=270: rows=338, invalid=1, invalid_pct=0.295858%
- position=271: rows=338, invalid=4, invalid_pct=1.183432%
- position=272: rows=338, invalid=1, invalid_pct=0.295858%
- position=273: rows=338, invalid=1, invalid_pct=0.295858%
- position=274: rows=338, invalid=1, invalid_pct=0.295858%
- position=275: rows=338, invalid=1, invalid_pct=0.295858%
- position=276: rows=338, invalid=1, invalid_pct=0.295858%
- position=277: rows=338, invalid=0, invalid_pct=0.000000%
- position=278: rows=337, invalid=1, invalid_pct=0.296736%
- position=279: rows=337, invalid=1, invalid_pct=0.296736%
- position=280: rows=337, invalid=1, invalid_pct=0.296736%
- position=281: rows=337, invalid=0, invalid_pct=0.000000%
- position=282: rows=337, invalid=2, invalid_pct=0.593472%
- position=283: rows=337, invalid=0, invalid_pct=0.000000%
- position=284: rows=337, invalid=0, invalid_pct=0.000000%
- position=285: rows=337, invalid=2, invalid_pct=0.593472%
- position=286: rows=337, invalid=1, invalid_pct=0.296736%
- position=287: rows=337, invalid=0, invalid_pct=0.000000%
- position=288: rows=337, invalid=1, invalid_pct=0.296736%
- position=289: rows=337, invalid=0, invalid_pct=0.000000%
- position=290: rows=337, invalid=0, invalid_pct=0.000000%
- position=291: rows=337, invalid=1, invalid_pct=0.296736%
- position=292: rows=337, invalid=0, invalid_pct=0.000000%
- position=293: rows=337, invalid=1, invalid_pct=0.296736%
- position=294: rows=337, invalid=2, invalid_pct=0.593472%
- position=295: rows=337, invalid=0, invalid_pct=0.000000%
- position=296: rows=337, invalid=0, invalid_pct=0.000000%
- position=297: rows=337, invalid=0, invalid_pct=0.000000%
- position=298: rows=337, invalid=0, invalid_pct=0.000000%
- position=299: rows=336, invalid=3, invalid_pct=0.892857%
- position=300: rows=336, invalid=0, invalid_pct=0.000000%
- position=301: rows=336, invalid=0, invalid_pct=0.000000%
- position=302: rows=336, invalid=2, invalid_pct=0.595238%
- position=303: rows=336, invalid=2, invalid_pct=0.595238%
- position=304: rows=336, invalid=3, invalid_pct=0.892857%
- position=305: rows=336, invalid=1, invalid_pct=0.297619%
- position=306: rows=336, invalid=0, invalid_pct=0.000000%
- position=307: rows=336, invalid=1, invalid_pct=0.297619%
- position=308: rows=336, invalid=1, invalid_pct=0.297619%
- position=309: rows=336, invalid=2, invalid_pct=0.595238%
- position=310: rows=336, invalid=1, invalid_pct=0.297619%
- position=311: rows=336, invalid=2, invalid_pct=0.595238%
- position=312: rows=336, invalid=1, invalid_pct=0.297619%
- position=313: rows=336, invalid=2, invalid_pct=0.595238%
- position=314: rows=336, invalid=3, invalid_pct=0.892857%
- position=315: rows=336, invalid=4, invalid_pct=1.190476%
- position=316: rows=336, invalid=4, invalid_pct=1.190476%
- position=317: rows=336, invalid=6, invalid_pct=1.785714%
- position=318: rows=336, invalid=2, invalid_pct=0.595238%
- position=319: rows=336, invalid=1, invalid_pct=0.297619%
- position=320: rows=336, invalid=4, invalid_pct=1.190476%
- position=321: rows=336, invalid=1, invalid_pct=0.297619%
- position=322: rows=336, invalid=2, invalid_pct=0.595238%
- position=323: rows=336, invalid=0, invalid_pct=0.000000%
- position=324: rows=336, invalid=1, invalid_pct=0.297619%
- position=325: rows=336, invalid=0, invalid_pct=0.000000%
- position=326: rows=336, invalid=1, invalid_pct=0.297619%
- position=327: rows=336, invalid=1, invalid_pct=0.297619%
- position=328: rows=336, invalid=2, invalid_pct=0.595238%
- position=329: rows=336, invalid=4, invalid_pct=1.190476%
- position=330: rows=336, invalid=3, invalid_pct=0.892857%
- position=331: rows=335, invalid=3, invalid_pct=0.895522%
- position=332: rows=335, invalid=2, invalid_pct=0.597015%
- position=333: rows=335, invalid=1, invalid_pct=0.298507%
- position=334: rows=335, invalid=3, invalid_pct=0.895522%
- position=335: rows=335, invalid=1, invalid_pct=0.298507%
- position=336: rows=335, invalid=0, invalid_pct=0.000000%
- position=337: rows=335, invalid=4, invalid_pct=1.194030%
- position=338: rows=335, invalid=4, invalid_pct=1.194030%
- position=339: rows=335, invalid=3, invalid_pct=0.895522%
- position=340: rows=334, invalid=3, invalid_pct=0.898204%
- position=341: rows=334, invalid=2, invalid_pct=0.598802%
- position=342: rows=334, invalid=1, invalid_pct=0.299401%
- position=343: rows=334, invalid=2, invalid_pct=0.598802%
- position=344: rows=334, invalid=1, invalid_pct=0.299401%
- position=345: rows=334, invalid=2, invalid_pct=0.598802%
- position=346: rows=334, invalid=1, invalid_pct=0.299401%
- position=347: rows=334, invalid=1, invalid_pct=0.299401%
- position=348: rows=334, invalid=2, invalid_pct=0.598802%
- position=349: rows=333, invalid=0, invalid_pct=0.000000%
- position=350: rows=333, invalid=2, invalid_pct=0.600601%
- position=351: rows=333, invalid=3, invalid_pct=0.900901%
- position=352: rows=333, invalid=0, invalid_pct=0.000000%
- position=353: rows=333, invalid=0, invalid_pct=0.000000%
- position=354: rows=333, invalid=2, invalid_pct=0.600601%
- position=355: rows=333, invalid=0, invalid_pct=0.000000%
- position=356: rows=333, invalid=4, invalid_pct=1.201201%
- position=357: rows=333, invalid=1, invalid_pct=0.300300%
- position=358: rows=333, invalid=1, invalid_pct=0.300300%
- position=359: rows=333, invalid=1, invalid_pct=0.300300%
- position=360: rows=333, invalid=0, invalid_pct=0.000000%
- position=361: rows=333, invalid=4, invalid_pct=1.201201%
- position=362: rows=333, invalid=1, invalid_pct=0.300300%
- position=363: rows=333, invalid=3, invalid_pct=0.900901%
- position=364: rows=333, invalid=0, invalid_pct=0.000000%
- position=365: rows=333, invalid=1, invalid_pct=0.300300%
- position=366: rows=333, invalid=2, invalid_pct=0.600601%
- position=367: rows=333, invalid=0, invalid_pct=0.000000%
- position=368: rows=333, invalid=1, invalid_pct=0.300300%
- position=369: rows=333, invalid=1, invalid_pct=0.300300%
- position=370: rows=333, invalid=1, invalid_pct=0.300300%
- position=371: rows=333, invalid=0, invalid_pct=0.000000%
- position=372: rows=333, invalid=3, invalid_pct=0.900901%
- position=373: rows=332, invalid=0, invalid_pct=0.000000%
- position=374: rows=332, invalid=2, invalid_pct=0.602410%
- position=375: rows=332, invalid=0, invalid_pct=0.000000%
- position=376: rows=331, invalid=0, invalid_pct=0.000000%
- position=377: rows=331, invalid=0, invalid_pct=0.000000%
- position=378: rows=331, invalid=2, invalid_pct=0.604230%
- position=379: rows=330, invalid=4, invalid_pct=1.212121%
- position=380: rows=330, invalid=0, invalid_pct=0.000000%
- position=381: rows=330, invalid=1, invalid_pct=0.303030%
- position=382: rows=330, invalid=2, invalid_pct=0.606061%
- position=383: rows=329, invalid=0, invalid_pct=0.000000%
- position=384: rows=329, invalid=0, invalid_pct=0.000000%
- position=385: rows=329, invalid=2, invalid_pct=0.607903%
- position=386: rows=329, invalid=1, invalid_pct=0.303951%
- position=387: rows=328, invalid=3, invalid_pct=0.914634%
- position=388: rows=328, invalid=1, invalid_pct=0.304878%
- position=389: rows=328, invalid=0, invalid_pct=0.000000%
- position=390: rows=327, invalid=1, invalid_pct=0.305810%
- position=391: rows=327, invalid=3, invalid_pct=0.917431%
- position=392: rows=327, invalid=0, invalid_pct=0.000000%
- position=393: rows=327, invalid=2, invalid_pct=0.611621%
- position=394: rows=327, invalid=1, invalid_pct=0.305810%
- position=395: rows=327, invalid=1, invalid_pct=0.305810%
- position=396: rows=327, invalid=0, invalid_pct=0.000000%
- position=397: rows=327, invalid=1, invalid_pct=0.305810%
- position=398: rows=327, invalid=2, invalid_pct=0.611621%
- position=399: rows=327, invalid=4, invalid_pct=1.223242%
- position=400: rows=327, invalid=3, invalid_pct=0.917431%
- position=401: rows=327, invalid=1, invalid_pct=0.305810%
- position=402: rows=327, invalid=1, invalid_pct=0.305810%
- position=403: rows=326, invalid=0, invalid_pct=0.000000%
- position=404: rows=326, invalid=2, invalid_pct=0.613497%
- position=405: rows=326, invalid=1, invalid_pct=0.306748%
- position=406: rows=326, invalid=1, invalid_pct=0.306748%
- position=407: rows=326, invalid=2, invalid_pct=0.613497%
- position=408: rows=326, invalid=1, invalid_pct=0.306748%
- position=409: rows=326, invalid=1, invalid_pct=0.306748%
- position=410: rows=326, invalid=0, invalid_pct=0.000000%
- position=411: rows=326, invalid=1, invalid_pct=0.306748%
- position=412: rows=326, invalid=2, invalid_pct=0.613497%
- position=413: rows=326, invalid=2, invalid_pct=0.613497%
- position=414: rows=325, invalid=2, invalid_pct=0.615385%
- position=415: rows=325, invalid=2, invalid_pct=0.615385%
- position=416: rows=325, invalid=1, invalid_pct=0.307692%
- position=417: rows=324, invalid=3, invalid_pct=0.925926%
- position=418: rows=323, invalid=1, invalid_pct=0.309598%
- position=419: rows=323, invalid=1, invalid_pct=0.309598%
- position=420: rows=323, invalid=2, invalid_pct=0.619195%
- position=421: rows=323, invalid=2, invalid_pct=0.619195%
- position=422: rows=323, invalid=1, invalid_pct=0.309598%
- position=423: rows=323, invalid=1, invalid_pct=0.309598%
- position=424: rows=323, invalid=1, invalid_pct=0.309598%
- position=425: rows=323, invalid=1, invalid_pct=0.309598%
- position=426: rows=323, invalid=0, invalid_pct=0.000000%
- position=427: rows=322, invalid=1, invalid_pct=0.310559%
- position=428: rows=322, invalid=0, invalid_pct=0.000000%
- position=429: rows=322, invalid=0, invalid_pct=0.000000%
- position=430: rows=322, invalid=1, invalid_pct=0.310559%
- position=431: rows=322, invalid=2, invalid_pct=0.621118%
- position=432: rows=322, invalid=2, invalid_pct=0.621118%
- position=433: rows=322, invalid=2, invalid_pct=0.621118%
- position=434: rows=322, invalid=1, invalid_pct=0.310559%
- position=435: rows=322, invalid=1, invalid_pct=0.310559%
- position=436: rows=322, invalid=3, invalid_pct=0.931677%
- position=437: rows=320, invalid=1, invalid_pct=0.312500%
- position=438: rows=320, invalid=0, invalid_pct=0.000000%
- position=439: rows=319, invalid=3, invalid_pct=0.940439%
- position=440: rows=318, invalid=0, invalid_pct=0.000000%
- position=441: rows=318, invalid=1, invalid_pct=0.314465%
- position=442: rows=318, invalid=2, invalid_pct=0.628931%
- position=443: rows=318, invalid=2, invalid_pct=0.628931%
- position=444: rows=318, invalid=1, invalid_pct=0.314465%
- position=445: rows=317, invalid=1, invalid_pct=0.315457%
- position=446: rows=316, invalid=5, invalid_pct=1.582278%
- position=447: rows=316, invalid=1, invalid_pct=0.316456%
- position=448: rows=316, invalid=3, invalid_pct=0.949367%
- position=449: rows=316, invalid=0, invalid_pct=0.000000%
- position=450: rows=315, invalid=2, invalid_pct=0.634921%
- position=451: rows=315, invalid=4, invalid_pct=1.269841%
- position=452: rows=315, invalid=0, invalid_pct=0.000000%
- position=453: rows=315, invalid=2, invalid_pct=0.634921%
- position=454: rows=315, invalid=2, invalid_pct=0.634921%
- position=455: rows=315, invalid=3, invalid_pct=0.952381%
- position=456: rows=315, invalid=0, invalid_pct=0.000000%
- position=457: rows=315, invalid=1, invalid_pct=0.317460%
- position=458: rows=315, invalid=1, invalid_pct=0.317460%
- position=459: rows=315, invalid=3, invalid_pct=0.952381%
- position=460: rows=314, invalid=3, invalid_pct=0.955414%
- position=461: rows=314, invalid=1, invalid_pct=0.318471%
- position=462: rows=314, invalid=2, invalid_pct=0.636943%
- position=463: rows=314, invalid=0, invalid_pct=0.000000%
- position=464: rows=314, invalid=1, invalid_pct=0.318471%
- position=465: rows=314, invalid=1, invalid_pct=0.318471%
- position=466: rows=313, invalid=1, invalid_pct=0.319489%
- position=467: rows=312, invalid=3, invalid_pct=0.961538%
- position=468: rows=312, invalid=3, invalid_pct=0.961538%
- position=469: rows=310, invalid=4, invalid_pct=1.290323%
- position=470: rows=309, invalid=3, invalid_pct=0.970874%
- position=471: rows=308, invalid=6, invalid_pct=1.948052%
- position=472: rows=308, invalid=1, invalid_pct=0.324675%
- position=473: rows=308, invalid=2, invalid_pct=0.649351%
- position=474: rows=308, invalid=1, invalid_pct=0.324675%
- position=475: rows=308, invalid=0, invalid_pct=0.000000%
- position=476: rows=308, invalid=1, invalid_pct=0.324675%
- position=477: rows=307, invalid=0, invalid_pct=0.000000%
- position=478: rows=307, invalid=2, invalid_pct=0.651466%
- position=479: rows=307, invalid=0, invalid_pct=0.000000%
- position=480: rows=307, invalid=2, invalid_pct=0.651466%
- position=481: rows=307, invalid=2, invalid_pct=0.651466%
- position=482: rows=307, invalid=0, invalid_pct=0.000000%
- position=483: rows=306, invalid=1, invalid_pct=0.326797%
- position=484: rows=306, invalid=1, invalid_pct=0.326797%
- position=485: rows=306, invalid=2, invalid_pct=0.653595%
- position=486: rows=306, invalid=0, invalid_pct=0.000000%
- position=487: rows=306, invalid=2, invalid_pct=0.653595%
- position=488: rows=306, invalid=0, invalid_pct=0.000000%
- position=489: rows=306, invalid=2, invalid_pct=0.653595%
- position=490: rows=306, invalid=3, invalid_pct=0.980392%
- position=491: rows=306, invalid=0, invalid_pct=0.000000%
- position=492: rows=306, invalid=1, invalid_pct=0.326797%
- position=493: rows=306, invalid=0, invalid_pct=0.000000%
- position=494: rows=306, invalid=1, invalid_pct=0.326797%
- position=495: rows=306, invalid=5, invalid_pct=1.633987%
- position=496: rows=306, invalid=0, invalid_pct=0.000000%
- position=497: rows=306, invalid=3, invalid_pct=0.980392%
- position=498: rows=306, invalid=1, invalid_pct=0.326797%
- position=499: rows=306, invalid=1, invalid_pct=0.326797%
- position=500: rows=304, invalid=0, invalid_pct=0.000000%
- position=501: rows=303, invalid=1, invalid_pct=0.330033%
- position=502: rows=303, invalid=2, invalid_pct=0.660066%
- position=503: rows=303, invalid=3, invalid_pct=0.990099%
- position=504: rows=302, invalid=1, invalid_pct=0.331126%
- position=505: rows=302, invalid=2, invalid_pct=0.662252%
- position=506: rows=302, invalid=0, invalid_pct=0.000000%
- position=507: rows=302, invalid=1, invalid_pct=0.331126%
- position=508: rows=301, invalid=1, invalid_pct=0.332226%
- position=509: rows=301, invalid=0, invalid_pct=0.000000%
- position=510: rows=301, invalid=0, invalid_pct=0.000000%
- position=511: rows=301, invalid=0, invalid_pct=0.000000%
- position=512: rows=301, invalid=2, invalid_pct=0.664452%
- position=513: rows=301, invalid=1, invalid_pct=0.332226%
- position=514: rows=301, invalid=0, invalid_pct=0.000000%
- position=515: rows=300, invalid=4, invalid_pct=1.333333%
- position=516: rows=300, invalid=3, invalid_pct=1.000000%
- position=517: rows=300, invalid=1, invalid_pct=0.333333%
- position=518: rows=300, invalid=2, invalid_pct=0.666667%
- position=519: rows=300, invalid=3, invalid_pct=1.000000%
- position=520: rows=300, invalid=0, invalid_pct=0.000000%
- position=521: rows=300, invalid=0, invalid_pct=0.000000%
- position=522: rows=300, invalid=0, invalid_pct=0.000000%
- position=523: rows=300, invalid=3, invalid_pct=1.000000%
- position=524: rows=300, invalid=0, invalid_pct=0.000000%
- position=525: rows=300, invalid=2, invalid_pct=0.666667%
- position=526: rows=300, invalid=0, invalid_pct=0.000000%
- position=527: rows=300, invalid=3, invalid_pct=1.000000%
- position=528: rows=300, invalid=1, invalid_pct=0.333333%
- position=529: rows=299, invalid=0, invalid_pct=0.000000%
- position=530: rows=299, invalid=0, invalid_pct=0.000000%
- position=531: rows=299, invalid=3, invalid_pct=1.003344%
- position=532: rows=299, invalid=1, invalid_pct=0.334448%
- position=533: rows=299, invalid=1, invalid_pct=0.334448%
- position=534: rows=299, invalid=0, invalid_pct=0.000000%
- position=535: rows=298, invalid=1, invalid_pct=0.335570%
- position=536: rows=298, invalid=2, invalid_pct=0.671141%
- position=537: rows=298, invalid=1, invalid_pct=0.335570%
- position=538: rows=298, invalid=0, invalid_pct=0.000000%
- position=539: rows=298, invalid=2, invalid_pct=0.671141%
- position=540: rows=298, invalid=2, invalid_pct=0.671141%
- position=541: rows=297, invalid=0, invalid_pct=0.000000%
- position=542: rows=297, invalid=1, invalid_pct=0.336700%
- position=543: rows=295, invalid=3, invalid_pct=1.016949%
- position=544: rows=295, invalid=1, invalid_pct=0.338983%
- position=545: rows=294, invalid=0, invalid_pct=0.000000%
- position=546: rows=294, invalid=1, invalid_pct=0.340136%
- position=547: rows=294, invalid=1, invalid_pct=0.340136%
- position=548: rows=294, invalid=0, invalid_pct=0.000000%
- position=549: rows=294, invalid=2, invalid_pct=0.680272%
- position=550: rows=293, invalid=1, invalid_pct=0.341297%
- position=551: rows=293, invalid=3, invalid_pct=1.023891%
- position=552: rows=293, invalid=2, invalid_pct=0.682594%
- position=553: rows=293, invalid=1, invalid_pct=0.341297%
- position=554: rows=293, invalid=0, invalid_pct=0.000000%
- position=555: rows=293, invalid=1, invalid_pct=0.341297%
- position=556: rows=293, invalid=0, invalid_pct=0.000000%
- position=557: rows=293, invalid=1, invalid_pct=0.341297%
- position=558: rows=293, invalid=0, invalid_pct=0.000000%
- position=559: rows=293, invalid=2, invalid_pct=0.682594%
- position=560: rows=293, invalid=1, invalid_pct=0.341297%
- position=561: rows=293, invalid=1, invalid_pct=0.341297%
- position=562: rows=293, invalid=0, invalid_pct=0.000000%
- position=563: rows=293, invalid=0, invalid_pct=0.000000%
- position=564: rows=292, invalid=0, invalid_pct=0.000000%
- position=565: rows=292, invalid=1, invalid_pct=0.342466%
- position=566: rows=292, invalid=0, invalid_pct=0.000000%
- position=567: rows=292, invalid=1, invalid_pct=0.342466%
- position=568: rows=291, invalid=1, invalid_pct=0.343643%
- position=569: rows=291, invalid=1, invalid_pct=0.343643%
- position=570: rows=290, invalid=1, invalid_pct=0.344828%
- position=571: rows=290, invalid=2, invalid_pct=0.689655%
- position=572: rows=289, invalid=0, invalid_pct=0.000000%
- position=573: rows=289, invalid=1, invalid_pct=0.346021%
- position=574: rows=289, invalid=2, invalid_pct=0.692042%
- position=575: rows=289, invalid=1, invalid_pct=0.346021%
- position=576: rows=288, invalid=0, invalid_pct=0.000000%
- position=577: rows=287, invalid=2, invalid_pct=0.696864%
- position=578: rows=285, invalid=0, invalid_pct=0.000000%
- position=579: rows=284, invalid=2, invalid_pct=0.704225%
- position=580: rows=284, invalid=1, invalid_pct=0.352113%
- position=581: rows=283, invalid=0, invalid_pct=0.000000%
- position=582: rows=281, invalid=0, invalid_pct=0.000000%
- position=583: rows=280, invalid=0, invalid_pct=0.000000%
- position=584: rows=280, invalid=0, invalid_pct=0.000000%
- position=585: rows=280, invalid=2, invalid_pct=0.714286%
- position=586: rows=280, invalid=0, invalid_pct=0.000000%
- position=587: rows=280, invalid=1, invalid_pct=0.357143%
- position=588: rows=280, invalid=0, invalid_pct=0.000000%
- position=589: rows=280, invalid=1, invalid_pct=0.357143%
- position=590: rows=280, invalid=2, invalid_pct=0.714286%
- position=591: rows=280, invalid=0, invalid_pct=0.000000%
- position=592: rows=278, invalid=0, invalid_pct=0.000000%
- position=593: rows=277, invalid=2, invalid_pct=0.722022%
- position=594: rows=276, invalid=2, invalid_pct=0.724638%
- position=595: rows=276, invalid=0, invalid_pct=0.000000%
- position=596: rows=274, invalid=1, invalid_pct=0.364964%
- position=597: rows=274, invalid=1, invalid_pct=0.364964%
- position=598: rows=274, invalid=0, invalid_pct=0.000000%
- position=599: rows=273, invalid=1, invalid_pct=0.366300%
- position=600: rows=273, invalid=1, invalid_pct=0.366300%
- position=601: rows=273, invalid=0, invalid_pct=0.000000%
- position=602: rows=271, invalid=0, invalid_pct=0.000000%
- position=603: rows=270, invalid=1, invalid_pct=0.370370%
- position=604: rows=269, invalid=1, invalid_pct=0.371747%
- position=605: rows=269, invalid=1, invalid_pct=0.371747%
- position=606: rows=269, invalid=1, invalid_pct=0.371747%
- position=607: rows=268, invalid=0, invalid_pct=0.000000%
- position=608: rows=268, invalid=0, invalid_pct=0.000000%
- position=609: rows=267, invalid=2, invalid_pct=0.749064%
- position=610: rows=267, invalid=0, invalid_pct=0.000000%
- position=611: rows=266, invalid=1, invalid_pct=0.375940%
- position=612: rows=266, invalid=3, invalid_pct=1.127820%
- position=613: rows=265, invalid=1, invalid_pct=0.377358%
- position=614: rows=263, invalid=2, invalid_pct=0.760456%
- position=615: rows=261, invalid=0, invalid_pct=0.000000%
- position=616: rows=259, invalid=0, invalid_pct=0.000000%
- position=617: rows=259, invalid=1, invalid_pct=0.386100%
- position=618: rows=258, invalid=1, invalid_pct=0.387597%
- position=619: rows=258, invalid=0, invalid_pct=0.000000%
- position=620: rows=258, invalid=0, invalid_pct=0.000000%
- position=621: rows=256, invalid=3, invalid_pct=1.171875%
- position=622: rows=255, invalid=1, invalid_pct=0.392157%
- position=623: rows=254, invalid=2, invalid_pct=0.787402%
- position=624: rows=254, invalid=3, invalid_pct=1.181102%
- position=625: rows=253, invalid=2, invalid_pct=0.790514%
- position=626: rows=253, invalid=1, invalid_pct=0.395257%
- position=627: rows=250, invalid=1, invalid_pct=0.400000%
- position=628: rows=249, invalid=2, invalid_pct=0.803213%
- position=629: rows=249, invalid=0, invalid_pct=0.000000%
- position=630: rows=249, invalid=0, invalid_pct=0.000000%
- position=631: rows=247, invalid=1, invalid_pct=0.404858%
- position=632: rows=247, invalid=2, invalid_pct=0.809717%
- position=633: rows=246, invalid=2, invalid_pct=0.813008%
- position=634: rows=244, invalid=1, invalid_pct=0.409836%
- position=635: rows=243, invalid=0, invalid_pct=0.000000%
- position=636: rows=240, invalid=0, invalid_pct=0.000000%
- position=637: rows=240, invalid=0, invalid_pct=0.000000%
- position=638: rows=240, invalid=0, invalid_pct=0.000000%
- position=639: rows=238, invalid=2, invalid_pct=0.840336%
- position=640: rows=236, invalid=2, invalid_pct=0.847458%
- position=641: rows=235, invalid=4, invalid_pct=1.702128%
- position=642: rows=235, invalid=1, invalid_pct=0.425532%
- position=643: rows=233, invalid=1, invalid_pct=0.429185%
- position=644: rows=231, invalid=0, invalid_pct=0.000000%
- position=645: rows=230, invalid=0, invalid_pct=0.000000%
- position=646: rows=229, invalid=1, invalid_pct=0.436681%
- position=647: rows=229, invalid=0, invalid_pct=0.000000%
- position=648: rows=228, invalid=3, invalid_pct=1.315789%
- position=649: rows=227, invalid=1, invalid_pct=0.440529%
- position=650: rows=227, invalid=0, invalid_pct=0.000000%
- position=651: rows=225, invalid=2, invalid_pct=0.888889%
- position=652: rows=224, invalid=1, invalid_pct=0.446429%
- position=653: rows=224, invalid=0, invalid_pct=0.000000%
- position=654: rows=224, invalid=0, invalid_pct=0.000000%
- position=655: rows=224, invalid=1, invalid_pct=0.446429%
- position=656: rows=224, invalid=1, invalid_pct=0.446429%
- position=657: rows=224, invalid=0, invalid_pct=0.000000%
- position=658: rows=224, invalid=1, invalid_pct=0.446429%
- position=659: rows=223, invalid=1, invalid_pct=0.448430%
- position=660: rows=222, invalid=0, invalid_pct=0.000000%
- position=661: rows=221, invalid=0, invalid_pct=0.000000%
- position=662: rows=220, invalid=1, invalid_pct=0.454545%
- position=663: rows=218, invalid=2, invalid_pct=0.917431%
- position=664: rows=217, invalid=0, invalid_pct=0.000000%
- position=665: rows=216, invalid=0, invalid_pct=0.000000%
- position=666: rows=216, invalid=1, invalid_pct=0.462963%
- position=667: rows=215, invalid=2, invalid_pct=0.930233%
- position=668: rows=210, invalid=1, invalid_pct=0.476190%
- position=669: rows=208, invalid=0, invalid_pct=0.000000%
- position=670: rows=206, invalid=0, invalid_pct=0.000000%
- position=671: rows=204, invalid=0, invalid_pct=0.000000%
- position=672: rows=203, invalid=1, invalid_pct=0.492611%
- position=673: rows=201, invalid=2, invalid_pct=0.995025%
- position=674: rows=200, invalid=1, invalid_pct=0.500000%
- position=675: rows=199, invalid=0, invalid_pct=0.000000%
- position=676: rows=199, invalid=0, invalid_pct=0.000000%
- position=677: rows=196, invalid=0, invalid_pct=0.000000%
- position=678: rows=196, invalid=1, invalid_pct=0.510204%
- position=679: rows=196, invalid=0, invalid_pct=0.000000%
- position=680: rows=195, invalid=3, invalid_pct=1.538462%
- position=681: rows=195, invalid=3, invalid_pct=1.538462%
- position=682: rows=194, invalid=0, invalid_pct=0.000000%
- position=683: rows=194, invalid=0, invalid_pct=0.000000%
- position=684: rows=192, invalid=1, invalid_pct=0.520833%
- position=685: rows=189, invalid=0, invalid_pct=0.000000%
- position=686: rows=188, invalid=2, invalid_pct=1.063830%
- position=687: rows=186, invalid=0, invalid_pct=0.000000%
- position=688: rows=185, invalid=2, invalid_pct=1.081081%
- position=689: rows=185, invalid=0, invalid_pct=0.000000%
- position=690: rows=185, invalid=0, invalid_pct=0.000000%
- position=691: rows=183, invalid=2, invalid_pct=1.092896%
- position=692: rows=180, invalid=3, invalid_pct=1.666667%
- position=693: rows=179, invalid=2, invalid_pct=1.117318%
- position=694: rows=179, invalid=1, invalid_pct=0.558659%
- position=695: rows=178, invalid=1, invalid_pct=0.561798%
- position=696: rows=178, invalid=1, invalid_pct=0.561798%
- position=697: rows=175, invalid=2, invalid_pct=1.142857%
- position=698: rows=173, invalid=0, invalid_pct=0.000000%
- position=699: rows=171, invalid=1, invalid_pct=0.584795%
- position=700: rows=169, invalid=2, invalid_pct=1.183432%
- position=701: rows=169, invalid=1, invalid_pct=0.591716%
- position=702: rows=169, invalid=0, invalid_pct=0.000000%
- position=703: rows=169, invalid=0, invalid_pct=0.000000%
- position=704: rows=169, invalid=1, invalid_pct=0.591716%
- position=705: rows=168, invalid=0, invalid_pct=0.000000%
- position=706: rows=166, invalid=0, invalid_pct=0.000000%
- position=707: rows=165, invalid=0, invalid_pct=0.000000%
- position=708: rows=164, invalid=0, invalid_pct=0.000000%
- position=709: rows=160, invalid=0, invalid_pct=0.000000%
- position=710: rows=159, invalid=1, invalid_pct=0.628931%
- position=711: rows=158, invalid=3, invalid_pct=1.898734%
- position=712: rows=157, invalid=0, invalid_pct=0.000000%
- position=713: rows=157, invalid=1, invalid_pct=0.636943%
- position=714: rows=154, invalid=0, invalid_pct=0.000000%
- position=715: rows=152, invalid=0, invalid_pct=0.000000%
- position=716: rows=151, invalid=0, invalid_pct=0.000000%
- position=717: rows=150, invalid=2, invalid_pct=1.333333%
- position=718: rows=149, invalid=0, invalid_pct=0.000000%
- position=719: rows=149, invalid=3, invalid_pct=2.013423%
- position=720: rows=149, invalid=0, invalid_pct=0.000000%
- position=721: rows=147, invalid=0, invalid_pct=0.000000%
- position=722: rows=147, invalid=0, invalid_pct=0.000000%
- position=723: rows=146, invalid=0, invalid_pct=0.000000%
- position=724: rows=146, invalid=1, invalid_pct=0.684932%
- position=725: rows=145, invalid=0, invalid_pct=0.000000%
- position=726: rows=144, invalid=0, invalid_pct=0.000000%
- position=727: rows=144, invalid=0, invalid_pct=0.000000%
- position=728: rows=142, invalid=0, invalid_pct=0.000000%
- position=729: rows=141, invalid=0, invalid_pct=0.000000%
- position=730: rows=141, invalid=1, invalid_pct=0.709220%
- position=731: rows=140, invalid=0, invalid_pct=0.000000%
- position=732: rows=138, invalid=0, invalid_pct=0.000000%
- position=733: rows=138, invalid=1, invalid_pct=0.724638%
- position=734: rows=137, invalid=0, invalid_pct=0.000000%
- position=735: rows=136, invalid=0, invalid_pct=0.000000%
- position=736: rows=135, invalid=1, invalid_pct=0.740741%
- position=737: rows=134, invalid=0, invalid_pct=0.000000%
- position=738: rows=133, invalid=2, invalid_pct=1.503759%
- position=739: rows=131, invalid=1, invalid_pct=0.763359%
- position=740: rows=128, invalid=0, invalid_pct=0.000000%
- position=741: rows=126, invalid=2, invalid_pct=1.587302%
- position=742: rows=126, invalid=0, invalid_pct=0.000000%
- position=743: rows=122, invalid=0, invalid_pct=0.000000%
- position=744: rows=121, invalid=1, invalid_pct=0.826446%
- position=745: rows=120, invalid=0, invalid_pct=0.000000%
- position=746: rows=119, invalid=0, invalid_pct=0.000000%
- position=747: rows=118, invalid=0, invalid_pct=0.000000%
- position=748: rows=118, invalid=0, invalid_pct=0.000000%
- position=749: rows=117, invalid=0, invalid_pct=0.000000%
- position=750: rows=114, invalid=0, invalid_pct=0.000000%
- position=751: rows=112, invalid=1, invalid_pct=0.892857%
- position=752: rows=112, invalid=0, invalid_pct=0.000000%
- position=753: rows=109, invalid=1, invalid_pct=0.917431%
- position=754: rows=106, invalid=1, invalid_pct=0.943396%
- position=755: rows=105, invalid=0, invalid_pct=0.000000%
- position=756: rows=105, invalid=0, invalid_pct=0.000000%
- position=757: rows=104, invalid=0, invalid_pct=0.000000%
- position=758: rows=102, invalid=0, invalid_pct=0.000000%
- position=759: rows=102, invalid=0, invalid_pct=0.000000%
- position=760: rows=102, invalid=1, invalid_pct=0.980392%
- position=761: rows=101, invalid=0, invalid_pct=0.000000%
- position=762: rows=100, invalid=1, invalid_pct=1.000000%
- position=763: rows=96, invalid=0, invalid_pct=0.000000%
- position=764: rows=95, invalid=0, invalid_pct=0.000000%
- position=765: rows=93, invalid=0, invalid_pct=0.000000%
- position=766: rows=93, invalid=0, invalid_pct=0.000000%
- position=767: rows=91, invalid=2, invalid_pct=2.197802%
- position=768: rows=90, invalid=0, invalid_pct=0.000000%
- position=769: rows=88, invalid=1, invalid_pct=1.136364%
- position=770: rows=86, invalid=0, invalid_pct=0.000000%
- position=771: rows=85, invalid=0, invalid_pct=0.000000%
- position=772: rows=85, invalid=0, invalid_pct=0.000000%
- position=773: rows=85, invalid=2, invalid_pct=2.352941%
- position=774: rows=84, invalid=0, invalid_pct=0.000000%
- position=775: rows=84, invalid=0, invalid_pct=0.000000%
- position=776: rows=84, invalid=0, invalid_pct=0.000000%
- position=777: rows=84, invalid=0, invalid_pct=0.000000%
- position=778: rows=84, invalid=0, invalid_pct=0.000000%
- position=779: rows=83, invalid=0, invalid_pct=0.000000%
- position=780: rows=80, invalid=0, invalid_pct=0.000000%
- position=781: rows=77, invalid=0, invalid_pct=0.000000%
- position=782: rows=77, invalid=0, invalid_pct=0.000000%
- position=783: rows=76, invalid=0, invalid_pct=0.000000%
- position=784: rows=76, invalid=0, invalid_pct=0.000000%
- position=785: rows=74, invalid=0, invalid_pct=0.000000%
- position=786: rows=73, invalid=0, invalid_pct=0.000000%
- position=787: rows=72, invalid=0, invalid_pct=0.000000%
- position=788: rows=71, invalid=0, invalid_pct=0.000000%
- position=789: rows=70, invalid=0, invalid_pct=0.000000%
- position=790: rows=70, invalid=1, invalid_pct=1.428571%
- position=791: rows=70, invalid=0, invalid_pct=0.000000%
- position=792: rows=68, invalid=0, invalid_pct=0.000000%
- position=793: rows=67, invalid=0, invalid_pct=0.000000%
- position=794: rows=66, invalid=0, invalid_pct=0.000000%
- position=795: rows=66, invalid=0, invalid_pct=0.000000%
- position=796: rows=66, invalid=1, invalid_pct=1.515152%
- position=797: rows=66, invalid=0, invalid_pct=0.000000%
- position=798: rows=65, invalid=0, invalid_pct=0.000000%
- position=799: rows=65, invalid=1, invalid_pct=1.538462%
- position=800: rows=63, invalid=0, invalid_pct=0.000000%
- position=801: rows=63, invalid=2, invalid_pct=3.174603%
- position=802: rows=61, invalid=0, invalid_pct=0.000000%
- position=803: rows=60, invalid=0, invalid_pct=0.000000%
- position=804: rows=59, invalid=0, invalid_pct=0.000000%
- position=805: rows=57, invalid=0, invalid_pct=0.000000%
- position=806: rows=56, invalid=0, invalid_pct=0.000000%
- position=807: rows=56, invalid=0, invalid_pct=0.000000%
- position=808: rows=54, invalid=1, invalid_pct=1.851852%
- position=809: rows=54, invalid=0, invalid_pct=0.000000%
- position=810: rows=54, invalid=1, invalid_pct=1.851852%
- position=811: rows=52, invalid=1, invalid_pct=1.923077%
- position=812: rows=52, invalid=0, invalid_pct=0.000000%
- position=813: rows=51, invalid=0, invalid_pct=0.000000%
- position=814: rows=51, invalid=0, invalid_pct=0.000000%
- position=815: rows=50, invalid=0, invalid_pct=0.000000%
- position=816: rows=49, invalid=0, invalid_pct=0.000000%
- position=817: rows=49, invalid=0, invalid_pct=0.000000%
- position=818: rows=49, invalid=0, invalid_pct=0.000000%
- position=819: rows=48, invalid=0, invalid_pct=0.000000%
- position=820: rows=45, invalid=0, invalid_pct=0.000000%
- position=821: rows=44, invalid=1, invalid_pct=2.272727%
- position=822: rows=44, invalid=0, invalid_pct=0.000000%
- position=823: rows=44, invalid=0, invalid_pct=0.000000%
- position=824: rows=44, invalid=1, invalid_pct=2.272727%
- position=825: rows=43, invalid=0, invalid_pct=0.000000%
- position=826: rows=42, invalid=0, invalid_pct=0.000000%
- position=827: rows=42, invalid=0, invalid_pct=0.000000%
- position=828: rows=42, invalid=0, invalid_pct=0.000000%
- position=829: rows=41, invalid=0, invalid_pct=0.000000%
- position=830: rows=39, invalid=0, invalid_pct=0.000000%
- position=831: rows=39, invalid=1, invalid_pct=2.564103%
- position=832: rows=39, invalid=0, invalid_pct=0.000000%
- position=833: rows=38, invalid=0, invalid_pct=0.000000%
- position=834: rows=38, invalid=0, invalid_pct=0.000000%
- position=835: rows=37, invalid=0, invalid_pct=0.000000%
- position=836: rows=37, invalid=0, invalid_pct=0.000000%
- position=837: rows=36, invalid=0, invalid_pct=0.000000%
- position=838: rows=36, invalid=0, invalid_pct=0.000000%
- position=839: rows=36, invalid=0, invalid_pct=0.000000%
- position=840: rows=36, invalid=0, invalid_pct=0.000000%
- position=841: rows=35, invalid=0, invalid_pct=0.000000%
- position=842: rows=35, invalid=0, invalid_pct=0.000000%
- position=843: rows=35, invalid=0, invalid_pct=0.000000%
- position=844: rows=32, invalid=0, invalid_pct=0.000000%
- position=845: rows=32, invalid=0, invalid_pct=0.000000%
- position=846: rows=32, invalid=0, invalid_pct=0.000000%
- position=847: rows=32, invalid=0, invalid_pct=0.000000%
- position=848: rows=32, invalid=0, invalid_pct=0.000000%
- position=849: rows=32, invalid=0, invalid_pct=0.000000%
- position=850: rows=32, invalid=0, invalid_pct=0.000000%
- position=851: rows=32, invalid=0, invalid_pct=0.000000%
- position=852: rows=30, invalid=0, invalid_pct=0.000000%
- position=853: rows=28, invalid=0, invalid_pct=0.000000%
- position=854: rows=28, invalid=0, invalid_pct=0.000000%
- position=855: rows=28, invalid=0, invalid_pct=0.000000%
- position=856: rows=28, invalid=0, invalid_pct=0.000000%
- position=857: rows=28, invalid=0, invalid_pct=0.000000%
- position=858: rows=28, invalid=0, invalid_pct=0.000000%
- position=859: rows=27, invalid=0, invalid_pct=0.000000%
- position=860: rows=27, invalid=0, invalid_pct=0.000000%
- position=861: rows=27, invalid=0, invalid_pct=0.000000%
- position=862: rows=25, invalid=1, invalid_pct=4.000000%
- position=863: rows=24, invalid=0, invalid_pct=0.000000%
- position=864: rows=23, invalid=0, invalid_pct=0.000000%
- position=865: rows=23, invalid=0, invalid_pct=0.000000%
- position=866: rows=23, invalid=0, invalid_pct=0.000000%
- position=867: rows=23, invalid=0, invalid_pct=0.000000%
- position=868: rows=21, invalid=0, invalid_pct=0.000000%
- position=869: rows=21, invalid=0, invalid_pct=0.000000%
- position=870: rows=21, invalid=0, invalid_pct=0.000000%
- position=871: rows=21, invalid=0, invalid_pct=0.000000%
- position=872: rows=21, invalid=0, invalid_pct=0.000000%
- position=873: rows=18, invalid=1, invalid_pct=5.555556%
- position=874: rows=18, invalid=0, invalid_pct=0.000000%
- position=875: rows=18, invalid=0, invalid_pct=0.000000%
- position=876: rows=18, invalid=0, invalid_pct=0.000000%
- position=877: rows=18, invalid=1, invalid_pct=5.555556%
- position=878: rows=18, invalid=0, invalid_pct=0.000000%
- position=879: rows=18, invalid=0, invalid_pct=0.000000%
- position=880: rows=18, invalid=0, invalid_pct=0.000000%
- position=881: rows=17, invalid=0, invalid_pct=0.000000%
- position=882: rows=17, invalid=0, invalid_pct=0.000000%
- position=883: rows=17, invalid=0, invalid_pct=0.000000%
- position=884: rows=17, invalid=0, invalid_pct=0.000000%
- position=885: rows=16, invalid=0, invalid_pct=0.000000%
- position=886: rows=15, invalid=0, invalid_pct=0.000000%
- position=887: rows=15, invalid=0, invalid_pct=0.000000%
- position=888: rows=15, invalid=0, invalid_pct=0.000000%
- position=889: rows=15, invalid=0, invalid_pct=0.000000%
- position=890: rows=15, invalid=0, invalid_pct=0.000000%
- position=891: rows=15, invalid=0, invalid_pct=0.000000%
- position=892: rows=15, invalid=0, invalid_pct=0.000000%
- position=893: rows=15, invalid=0, invalid_pct=0.000000%
- position=894: rows=15, invalid=0, invalid_pct=0.000000%
- position=895: rows=15, invalid=0, invalid_pct=0.000000%
- position=896: rows=15, invalid=0, invalid_pct=0.000000%
- position=897: rows=15, invalid=0, invalid_pct=0.000000%
- position=898: rows=15, invalid=0, invalid_pct=0.000000%
- position=899: rows=15, invalid=0, invalid_pct=0.000000%
- position=900: rows=15, invalid=0, invalid_pct=0.000000%
- position=901: rows=15, invalid=0, invalid_pct=0.000000%
- position=902: rows=15, invalid=0, invalid_pct=0.000000%
- position=903: rows=15, invalid=0, invalid_pct=0.000000%
- position=904: rows=15, invalid=0, invalid_pct=0.000000%
- position=905: rows=15, invalid=0, invalid_pct=0.000000%
- position=906: rows=15, invalid=0, invalid_pct=0.000000%
- position=907: rows=15, invalid=0, invalid_pct=0.000000%
- position=908: rows=15, invalid=0, invalid_pct=0.000000%
- position=909: rows=15, invalid=1, invalid_pct=6.666667%
- position=910: rows=15, invalid=0, invalid_pct=0.000000%
- position=911: rows=15, invalid=0, invalid_pct=0.000000%
- position=912: rows=15, invalid=0, invalid_pct=0.000000%
- position=913: rows=15, invalid=0, invalid_pct=0.000000%
- position=914: rows=15, invalid=0, invalid_pct=0.000000%
- position=915: rows=14, invalid=0, invalid_pct=0.000000%
- position=916: rows=14, invalid=0, invalid_pct=0.000000%
- position=917: rows=14, invalid=0, invalid_pct=0.000000%
- position=918: rows=14, invalid=0, invalid_pct=0.000000%
- position=919: rows=14, invalid=0, invalid_pct=0.000000%
- position=920: rows=13, invalid=0, invalid_pct=0.000000%
- position=921: rows=13, invalid=0, invalid_pct=0.000000%
- position=922: rows=13, invalid=0, invalid_pct=0.000000%
- position=923: rows=13, invalid=0, invalid_pct=0.000000%
- position=924: rows=13, invalid=0, invalid_pct=0.000000%
- position=925: rows=12, invalid=0, invalid_pct=0.000000%
- position=926: rows=12, invalid=0, invalid_pct=0.000000%
- position=927: rows=12, invalid=0, invalid_pct=0.000000%
- position=928: rows=12, invalid=0, invalid_pct=0.000000%
- position=929: rows=12, invalid=0, invalid_pct=0.000000%
- position=930: rows=12, invalid=0, invalid_pct=0.000000%
- position=931: rows=12, invalid=0, invalid_pct=0.000000%
- position=932: rows=11, invalid=0, invalid_pct=0.000000%
- position=933: rows=11, invalid=0, invalid_pct=0.000000%
- position=934: rows=11, invalid=0, invalid_pct=0.000000%
- position=935: rows=11, invalid=0, invalid_pct=0.000000%
- position=936: rows=11, invalid=0, invalid_pct=0.000000%
- position=937: rows=11, invalid=0, invalid_pct=0.000000%
- position=938: rows=11, invalid=0, invalid_pct=0.000000%
- position=939: rows=10, invalid=0, invalid_pct=0.000000%
- position=940: rows=10, invalid=0, invalid_pct=0.000000%
- position=941: rows=10, invalid=0, invalid_pct=0.000000%
- position=942: rows=10, invalid=0, invalid_pct=0.000000%
- position=943: rows=10, invalid=0, invalid_pct=0.000000%
- position=944: rows=9, invalid=0, invalid_pct=0.000000%
- position=945: rows=9, invalid=0, invalid_pct=0.000000%
- position=946: rows=9, invalid=0, invalid_pct=0.000000%
- position=947: rows=9, invalid=0, invalid_pct=0.000000%
- position=948: rows=8, invalid=0, invalid_pct=0.000000%
- position=949: rows=8, invalid=0, invalid_pct=0.000000%
- position=950: rows=8, invalid=0, invalid_pct=0.000000%
- position=951: rows=6, invalid=0, invalid_pct=0.000000%
- position=952: rows=6, invalid=0, invalid_pct=0.000000%
- position=953: rows=6, invalid=0, invalid_pct=0.000000%
- position=954: rows=6, invalid=0, invalid_pct=0.000000%
- position=955: rows=6, invalid=0, invalid_pct=0.000000%
- position=956: rows=5, invalid=0, invalid_pct=0.000000%
- position=957: rows=5, invalid=0, invalid_pct=0.000000%
- position=958: rows=5, invalid=0, invalid_pct=0.000000%
- position=959: rows=5, invalid=0, invalid_pct=0.000000%
- position=960: rows=5, invalid=0, invalid_pct=0.000000%
- position=961: rows=5, invalid=0, invalid_pct=0.000000%
- position=962: rows=4, invalid=0, invalid_pct=0.000000%
- position=963: rows=4, invalid=0, invalid_pct=0.000000%
- position=964: rows=4, invalid=0, invalid_pct=0.000000%
- position=965: rows=4, invalid=0, invalid_pct=0.000000%
- position=966: rows=4, invalid=0, invalid_pct=0.000000%
- position=967: rows=4, invalid=0, invalid_pct=0.000000%
- position=968: rows=4, invalid=0, invalid_pct=0.000000%
- position=969: rows=4, invalid=0, invalid_pct=0.000000%
- position=970: rows=4, invalid=0, invalid_pct=0.000000%
- position=971: rows=4, invalid=0, invalid_pct=0.000000%
- position=972: rows=4, invalid=0, invalid_pct=0.000000%
- position=973: rows=3, invalid=0, invalid_pct=0.000000%
- position=974: rows=3, invalid=0, invalid_pct=0.000000%
- position=975: rows=3, invalid=0, invalid_pct=0.000000%
- position=976: rows=3, invalid=0, invalid_pct=0.000000%
- position=977: rows=2, invalid=0, invalid_pct=0.000000%
- position=978: rows=2, invalid=0, invalid_pct=0.000000%
- position=979: rows=2, invalid=0, invalid_pct=0.000000%
- position=980: rows=2, invalid=0, invalid_pct=0.000000%
- position=981: rows=2, invalid=0, invalid_pct=0.000000%
- position=982: rows=2, invalid=0, invalid_pct=0.000000%
- position=983: rows=1, invalid=0, invalid_pct=0.000000%
- position=984: rows=1, invalid=0, invalid_pct=0.000000%
- position=985: rows=1, invalid=0, invalid_pct=0.000000%
- position=986: rows=1, invalid=0, invalid_pct=0.000000%
- position=987: rows=1, invalid=0, invalid_pct=0.000000%
- position=988: rows=1, invalid=0, invalid_pct=0.000000%
- position=989: rows=1, invalid=0, invalid_pct=0.000000%
- position=990: rows=1, invalid=0, invalid_pct=0.000000%
- position=991: rows=1, invalid=0, invalid_pct=0.000000%
- position=992: rows=1, invalid=0, invalid_pct=0.000000%
- position=993: rows=1, invalid=0, invalid_pct=0.000000%
- position=994: rows=1, invalid=0, invalid_pct=0.000000%
- position=995: rows=1, invalid=0, invalid_pct=0.000000%
- position=996: rows=1, invalid=0, invalid_pct=0.000000%
- position=997: rows=1, invalid=0, invalid_pct=0.000000%
- position=998: rows=1, invalid=0, invalid_pct=0.000000%
- position=999: rows=1, invalid=0, invalid_pct=0.000000%
- position=1000: rows=1, invalid=0, invalid_pct=0.000000%
- position=1001: rows=1, invalid=0, invalid_pct=0.000000%
- position=1002: rows=1, invalid=0, invalid_pct=0.000000%
- position=1003: rows=1, invalid=0, invalid_pct=0.000000%
- position=1004: rows=1, invalid=0, invalid_pct=0.000000%
- position=1005: rows=1, invalid=0, invalid_pct=0.000000%
- position=1006: rows=1, invalid=0, invalid_pct=0.000000%
- position=1007: rows=1, invalid=0, invalid_pct=0.000000%
- position=1008: rows=1, invalid=0, invalid_pct=0.000000%
- position=1009: rows=1, invalid=0, invalid_pct=0.000000%
- position=1010: rows=1, invalid=0, invalid_pct=0.000000%
- position=1011: rows=1, invalid=0, invalid_pct=0.000000%
- position=1012: rows=1, invalid=0, invalid_pct=0.000000%
- position=1013: rows=1, invalid=0, invalid_pct=0.000000%
- position=1014: rows=1, invalid=0, invalid_pct=0.000000%
- position=1015: rows=1, invalid=0, invalid_pct=0.000000%
- position=1016: rows=1, invalid=0, invalid_pct=0.000000%
- position=1017: rows=1, invalid=0, invalid_pct=0.000000%
- position=1018: rows=1, invalid=0, invalid_pct=0.000000%
- position=1019: rows=1, invalid=0, invalid_pct=0.000000%
- position=1020: rows=1, invalid=0, invalid_pct=0.000000%
- position=1021: rows=1, invalid=0, invalid_pct=0.000000%
- position=1022: rows=1, invalid=0, invalid_pct=0.000000%
- position=1023: rows=1, invalid=0, invalid_pct=0.000000%
- position=1024: rows=1, invalid=0, invalid_pct=0.000000%
- position=1025: rows=1, invalid=0, invalid_pct=0.000000%
- position=1026: rows=1, invalid=0, invalid_pct=0.000000%
- position=1027: rows=1, invalid=0, invalid_pct=0.000000%
- position=1028: rows=1, invalid=0, invalid_pct=0.000000%
- position=1029: rows=1, invalid=0, invalid_pct=0.000000%
- position=1030: rows=1, invalid=0, invalid_pct=0.000000%
- position=1031: rows=1, invalid=0, invalid_pct=0.000000%
- position=1032: rows=1, invalid=0, invalid_pct=0.000000%
- position=1033: rows=1, invalid=0, invalid_pct=0.000000%
- position=1034: rows=1, invalid=0, invalid_pct=0.000000%
- position=1035: rows=1, invalid=0, invalid_pct=0.000000%
- position=1036: rows=1, invalid=0, invalid_pct=0.000000%
- position=1037: rows=1, invalid=0, invalid_pct=0.000000%
- position=1038: rows=1, invalid=0, invalid_pct=0.000000%
- position=1039: rows=1, invalid=0, invalid_pct=0.000000%
- position=1040: rows=1, invalid=0, invalid_pct=0.000000%
- position=1041: rows=1, invalid=0, invalid_pct=0.000000%
- position=1042: rows=1, invalid=0, invalid_pct=0.000000%
- position=1043: rows=1, invalid=0, invalid_pct=0.000000%
- position=1044: rows=1, invalid=0, invalid_pct=0.000000%
- position=1045: rows=1, invalid=0, invalid_pct=0.000000%
- position=1046: rows=1, invalid=0, invalid_pct=0.000000%
- position=1047: rows=1, invalid=0, invalid_pct=0.000000%
- position=1048: rows=1, invalid=0, invalid_pct=0.000000%
- position=1049: rows=1, invalid=0, invalid_pct=0.000000%
- position=1050: rows=1, invalid=0, invalid_pct=0.000000%
- position=1051: rows=1, invalid=0, invalid_pct=0.000000%

## Full List of Flagged Rows
trace_id,step,position,token_id,q,draft_top1_prob,violation_magnitude,post_rejection_row,dataset
trace_livecodebench_0.jsonl,204,204,272,0.0459895059466362,0.042919132858514786,0.003070373088121414,False,livecodebench
trace_livecodebench_0.jsonl,321,321,11,0.01053994707763195,0.007816155441105366,0.0027237916365265846,True,livecodebench
trace_livecodebench_1.jsonl,159,159,220,0.32584384083747864,0.09709832072257996,0.22874552011489868,False,livecodebench
trace_livecodebench_1.jsonl,171,171,220,0.5413999557495117,0.12443342804908752,0.4169665277004242,True,livecodebench
trace_livecodebench_1.jsonl,273,273,2027,0.0513024665415287,0.040318798273801804,0.010983668267726898,True,livecodebench
trace_livecodebench_1.jsonl,315,315,220,0.46603095531463623,0.26731276512145996,0.19871819019317627,False,livecodebench
trace_livecodebench_1.jsonl,560,560,220,0.037855736911296844,0.026701195165514946,0.011154541745781898,False,livecodebench
trace_livecodebench_1.jsonl,609,609,11,0.10961141437292099,0.028590310364961624,0.08102110400795937,True,livecodebench
trace_livecodebench_3.jsonl,57,57,11,0.06307771056890488,0.025829192250967026,0.03724851831793785,True,livecodebench
trace_livecodebench_3.jsonl,108,108,11,0.18194334208965302,0.08568895608186722,0.0962543860077858,True,livecodebench
trace_livecodebench_3.jsonl,158,158,11,0.031480804085731506,0.010194187983870506,0.021286616101861,False,livecodebench
trace_livecodebench_4.jsonl,188,188,374,0.041701313108205795,0.033036038279533386,0.008665274828672409,False,livecodebench
trace_livecodebench_4.jsonl,202,202,220,0.4787597954273224,0.4742153584957123,0.004544436931610107,False,livecodebench
trace_livecodebench_5.jsonl,199,199,220,0.7581033110618591,0.18264783918857574,0.5754554718732834,True,livecodebench
trace_livecodebench_6.jsonl,54,54,6811,0.020547877997159958,0.0160377100110054,0.004510167986154556,False,livecodebench
trace_livecodebench_6.jsonl,339,339,279,0.07511148601770401,0.0160377100110054,0.05907377600669861,False,livecodebench
trace_livecodebench_6.jsonl,356,356,8,0.1242835596203804,0.07562024146318436,0.048663318157196045,True,livecodebench
trace_livecodebench_7.jsonl,95,95,374,0.03756081685423851,0.020432570949196815,0.017128245905041695,True,livecodebench
trace_livecodebench_8.jsonl,9,9,382,0.08627323806285858,0.05320548638701439,0.03306775167584419,False,livecodebench
trace_livecodebench_8.jsonl,120,120,320,0.281271368265152,0.0586635023355484,0.22260786592960358,False,livecodebench
trace_livecodebench_9.jsonl,46,46,311,0.2769539952278137,0.13271766901016235,0.14423632621765137,True,livecodebench
trace_livecodebench_10.jsonl,122,122,11,0.3789963126182556,0.052585624158382416,0.3264106884598732,True,livecodebench
trace_livecodebench_10.jsonl,247,247,1855,0.07343164086341858,0.061119645833969116,0.012311995029449463,False,livecodebench
trace_livecodebench_11.jsonl,226,226,311,0.20303848385810852,0.17582234740257263,0.02721613645553589,False,livecodebench
trace_livecodebench_11.jsonl,391,391,311,0.3245271146297455,0.1710798293352127,0.15344728529453278,False,livecodebench
trace_livecodebench_11.jsonl,460,460,1396,0.6128283143043518,0.24102574586868286,0.37180256843566895,True,livecodebench
trace_livecodebench_11.jsonl,668,668,311,0.27320870757102966,0.21208222210407257,0.06112648546695709,True,livecodebench
trace_livecodebench_11.jsonl,811,811,220,0.22735442221164703,0.19291457533836365,0.034439846873283386,True,livecodebench
trace_livecodebench_12.jsonl,62,62,220,0.13368037343025208,0.06966463476419449,0.06401573866605759,False,livecodebench
trace_livecodebench_12.jsonl,445,445,1396,0.15206998586654663,0.14113931357860565,0.010930672287940979,False,livecodebench
trace_livecodebench_12.jsonl,641,641,11,0.07296640425920486,0.05207459256052971,0.020891811698675156,True,livecodebench
trace_livecodebench_12.jsonl,753,753,220,0.028950607404112816,0.02153898775577545,0.007411619648337364,True,livecodebench
trace_livecodebench_13.jsonl,516,516,11,0.06241314113140106,0.026701195165514946,0.035711945965886116,True,livecodebench
trace_livecodebench_13.jsonl,528,528,11,0.040495615452528,0.03642499819397926,0.004070617258548737,True,livecodebench
trace_livecodebench_13.jsonl,539,539,384,0.09489893168210983,0.03847246617078781,0.05642646551132202,False,livecodebench
trace_livecodebench_14.jsonl,229,229,11,0.08602249622344971,0.08305259048938751,0.002969905734062195,False,livecodebench
trace_livecodebench_14.jsonl,241,241,11,0.07535229623317719,0.026082664728164673,0.04926963150501251,False,livecodebench
trace_livecodebench_14.jsonl,271,271,220,0.5363251566886902,0.32465246319770813,0.21167269349098206,False,livecodebench
trace_livecodebench_14.jsonl,294,294,220,0.72353595495224,0.6410934329032898,0.0824425220489502,False,livecodebench
trace_livecodebench_14.jsonl,334,334,1473,0.09454462677240372,0.051067378371953964,0.04347724840044975,False,livecodebench
trace_livecodebench_14.jsonl,339,339,220,0.22860495746135712,0.14561955630779266,0.08298540115356445,True,livecodebench
trace_livecodebench_14.jsonl,543,543,220,0.06553345918655396,0.0475071519613266,0.018026307225227356,True,livecodebench
trace_livecodebench_14.jsonl,565,565,220,0.49810290336608887,0.2699360251426697,0.2281668782234192,False,livecodebench
trace_livecodebench_17.jsonl,263,263,1963,0.13811838626861572,0.11666630208492279,0.021452084183692932,True,livecodebench
trace_livecodebench_17.jsonl,543,543,279,0.38945266604423523,0.044891104102134705,0.3445615619421005,False,livecodebench
trace_livecodebench_18.jsonl,16,16,279,0.27125656604766846,0.10096627473831177,0.1702902913093567,False,livecodebench
trace_livecodebench_18.jsonl,469,469,11,0.04820001870393753,0.039307963103055954,0.008892055600881577,True,livecodebench
trace_livecodebench_18.jsonl,649,649,279,0.4066418707370758,0.3412310779094696,0.0654107928276062,False,livecodebench
trace_livecodebench_19.jsonl,379,379,11,0.1938074678182602,0.025132494047284126,0.16867497377097607,True,livecodebench
trace_livecodebench_19.jsonl,404,404,11,0.02223403938114643,0.02055264636874199,0.0016813930124044418,True,livecodebench
trace_livecodebench_20.jsonl,646,646,5037,0.6446506381034851,0.47121474146842957,0.17343589663505554,False,livecodebench
trace_livecodebench_20.jsonl,744,744,374,0.0880984365940094,0.06455521285533905,0.02354322373867035,False,livecodebench
trace_livecodebench_21.jsonl,17,17,279,0.3139120042324066,0.195570170879364,0.1183418333530426,True,livecodebench
trace_livecodebench_21.jsonl,195,195,320,0.17565244436264038,0.16292698681354523,0.012725457549095154,False,livecodebench
trace_livecodebench_21.jsonl,419,419,220,0.10779745876789093,0.08910242468118668,0.018695034086704254,True,livecodebench
trace_livecodebench_22.jsonl,409,409,220,0.16881023347377777,0.07940427213907242,0.08940596133470535,True,livecodebench
trace_livecodebench_22.jsonl,459,459,220,0.08098791539669037,0.03692641481757164,0.04406150057911873,True,livecodebench
trace_livecodebench_23.jsonl,105,105,11,0.2596762180328369,0.0851883515715599,0.174487866461277,False,livecodebench
trace_livecodebench_23.jsonl,328,328,13,0.108334481716156,0.04410889744758606,0.06422558426856995,False,livecodebench
trace_livecodebench_23.jsonl,625,625,5603,0.24341267347335815,0.03977131471037865,0.2036413587629795,True,livecodebench
trace_livecodebench_25.jsonl,248,248,279,0.180490642786026,0.14113931357860565,0.03935132920742035,True,livecodebench
trace_livecodebench_25.jsonl,279,279,279,0.18504777550697327,0.0851883515715599,0.09985942393541336,False,livecodebench
trace_livecodebench_25.jsonl,623,623,369,0.05894666910171509,0.03885000944137573,0.020096659660339355,True,livecodebench
trace_livecodebench_26.jsonl,29,29,5784,0.09473828971385956,0.07229841500520706,0.022439874708652496,True,livecodebench
trace_livecodebench_27.jsonl,165,165,5603,0.049327973276376724,0.04428153485059738,0.005046438425779343,False,livecodebench
trace_livecodebench_27.jsonl,320,320,5603,0.20036455988883972,0.17946529388427734,0.020899266004562378,False,livecodebench
trace_livecodebench_27.jsonl,446,446,2997,0.03689246624708176,0.031832560896873474,0.0050599053502082825,False,livecodebench
trace_livecodebench_27.jsonl,724,724,374,0.07795670628547668,0.0588931068778038,0.019063599407672882,True,livecodebench
trace_livecodebench_28.jsonl,387,387,433,0.23134835064411163,0.22886812686920166,0.002480223774909973,False,livecodebench
trace_livecodebench_29.jsonl,140,140,364,0.31200075149536133,0.12863436341285706,0.18336638808250427,True,livecodebench
trace_livecodebench_29.jsonl,316,316,364,0.032082393765449524,0.025829192250967026,0.006253201514482498,False,livecodebench
trace_livecodebench_29.jsonl,435,435,279,0.18677978217601776,0.1194329708814621,0.06734681129455566,False,livecodebench
trace_livecodebench_29.jsonl,597,597,11,0.07400639355182648,0.046770624816417694,0.027235768735408783,False,livecodebench
trace_livecodebench_30.jsonl,773,773,311,0.09718931466341019,0.056416142731904984,0.0407731719315052,True,livecodebench
trace_livecodebench_31.jsonl,10,10,264,0.6679843068122864,0.17445406317710876,0.4935302436351776,False,livecodebench
trace_livecodebench_31.jsonl,54,54,279,0.5963971614837646,0.07062362134456635,0.5257735401391983,True,livecodebench
trace_livecodebench_31.jsonl,211,211,842,0.5710982084274292,0.5522524118423462,0.018845796585083008,True,livecodebench
trace_livecodebench_31.jsonl,738,738,842,0.6524924039840698,0.22976388037204742,0.4227285236120224,True,livecodebench
trace_livecodebench_32.jsonl,25,25,430,0.02560858614742756,0.02328919805586338,0.0023193880915641785,False,livecodebench
trace_livecodebench_32.jsonl,99,99,311,0.26888027787208557,0.26523253321647644,0.003647744655609131,False,livecodebench
trace_livecodebench_32.jsonl,106,106,220,0.32326698303222656,0.24220550060272217,0.0810614824295044,True,livecodebench
trace_livecodebench_33.jsonl,207,207,11,0.03721138462424278,0.030973929911851883,0.0062374547123909,False,livecodebench
trace_livecodebench_33.jsonl,221,221,279,0.0542183555662632,0.04217129200696945,0.012047063559293747,False,livecodebench
trace_livecodebench_33.jsonl,272,272,279,0.1339433491230011,0.03496122732758522,0.09898212179541588,False,livecodebench
trace_livecodebench_33.jsonl,302,302,7677,0.18048137426376343,0.1194329708814621,0.06104840338230133,False,livecodebench
trace_livecodebench_33.jsonl,316,316,11,0.21608246862888336,0.03401820734143257,0.1820642612874508,False,livecodebench
trace_livecodebench_33.jsonl,589,589,24894,0.1311948150396347,0.07343694567680359,0.057757869362831116,False,livecodebench
trace_livecodebench_35.jsonl,15,15,13,0.20358410477638245,0.10136144608259201,0.10222265869379044,True,livecodebench
trace_livecodebench_35.jsonl,34,34,11,0.36852532625198364,0.03140031173825264,0.337125014513731,False,livecodebench
trace_livecodebench_35.jsonl,97,97,364,0.06957755237817764,0.021040037274360657,0.048537515103816986,False,livecodebench
trace_livecodebench_35.jsonl,215,215,11,0.12282717227935791,0.021329669281840324,0.10149750299751759,True,livecodebench
trace_livecodebench_35.jsonl,258,258,311,0.07934500277042389,0.030434222891926765,0.048910779878497124,True,livecodebench
trace_livecodebench_35.jsonl,594,594,311,0.017320552840828896,0.010683417320251465,0.006637135520577431,True,livecodebench
trace_livecodebench_35.jsonl,667,667,264,0.07391075044870377,0.07090003043413162,0.0030107200145721436,False,livecodebench
trace_livecodebench_38.jsonl,497,497,279,0.3378535211086273,0.1495102047920227,0.18834331631660461,True,livecodebench
trace_livecodebench_39.jsonl,32,32,311,0.25088149309158325,0.016354024410247803,0.23452746868133545,True,livecodebench
trace_livecodebench_40.jsonl,121,121,220,0.3401546776294708,0.21500170230865479,0.12515297532081604,False,livecodebench
trace_livecodebench_40.jsonl,216,216,220,0.24720658361911774,0.16276796162128448,0.08443862199783325,True,livecodebench
trace_livecodebench_40.jsonl,455,455,220,0.8591454029083252,0.4511756896972656,0.40796971321105957,False,livecodebench
trace_livecodebench_40.jsonl,542,542,220,0.329435259103775,0.2031623274087906,0.12627293169498444,False,livecodebench
trace_livecodebench_40.jsonl,614,614,220,0.42691200971603394,0.3199315071105957,0.10698050260543823,False,livecodebench
trace_livecodebench_40.jsonl,672,672,11,0.05734129995107651,0.05156852304935455,0.005772776901721954,False,livecodebench
trace_livecodebench_40.jsonl,681,681,220,0.8150779604911804,0.7200971841812134,0.09498077630996704,False,livecodebench
trace_livecodebench_41.jsonl,316,316,311,0.20992453396320343,0.08289053291082382,0.1270340010523796,True,livecodebench
trace_livecodebench_42.jsonl,250,250,11,0.5280073285102844,0.302609384059906,0.22539794445037842,False,livecodebench
trace_livecodebench_42.jsonl,483,483,311,0.048083748668432236,0.04135562479496002,0.006728123873472214,True,livecodebench
trace_livecodebench_43.jsonl,459,459,20,0.19922101497650146,0.04055573418736458,0.1586652807891369,False,livecodebench
trace_livecodebench_44.jsonl,361,361,279,0.23449254035949707,0.1988440603017807,0.03564848005771637,False,livecodebench
trace_livecodebench_45.jsonl,544,544,220,0.5222638845443726,0.2039574682712555,0.31830641627311707,False,livecodebench
trace_livecodebench_45.jsonl,551,551,220,0.5326911807060242,0.17876562476158142,0.35392555594444275,False,livecodebench
trace_livecodebench_45.jsonl,579,579,220,0.2542423903942108,0.09634269028902054,0.15789970010519028,False,livecodebench
trace_livecodebench_45.jsonl,696,696,220,0.46954649686813354,0.4616495370864868,0.007896959781646729,False,livecodebench
trace_livecodebench_48.jsonl,51,51,2015,0.04547911509871483,0.03271498903632164,0.012764126062393188,False,livecodebench
trace_livecodebench_48.jsonl,484,484,925,0.017953436821699142,0.01654680073261261,0.0014066360890865326,False,livecodebench
trace_livecodebench_49.jsonl,146,146,439,0.5082506537437439,0.3037937581539154,0.2044568955898285,True,livecodebench
trace_livecodebench_49.jsonl,523,523,482,0.09436244517564774,0.03977131471037865,0.05459113046526909,False,livecodebench
trace_livecodebench_50.jsonl,320,320,374,0.2439202219247818,0.24102574586868286,0.002894476056098938,False,livecodebench
trace_livecodebench_50.jsonl,495,495,279,0.5457495450973511,0.45007553696632385,0.09567400813102722,False,livecodebench
trace_livecodebench_50.jsonl,569,569,17,0.10297106206417084,0.034824926406145096,0.06814613565802574,False,livecodebench
trace_livecodebench_51.jsonl,59,59,311,0.6412448287010193,0.24626006186008453,0.39498476684093475,False,livecodebench
trace_livecodebench_52.jsonl,240,240,279,0.4448378384113312,0.10295765101909637,0.3418801873922348,True,livecodebench
trace_livecodebench_52.jsonl,282,282,832,0.12317952513694763,0.11530710011720657,0.007872425019741058,True,livecodebench
trace_livecodebench_53.jsonl,130,130,279,0.2827364206314087,0.018315639346837997,0.2644207812845707,True,livecodebench
trace_livecodebench_53.jsonl,193,193,374,0.08140666782855988,0.06778554618358612,0.013621121644973755,False,livecodebench
trace_livecodebench_53.jsonl,230,230,279,0.0887666642665863,0.012886662036180496,0.07588000223040581,False,livecodebench
trace_livecodebench_53.jsonl,304,304,1212,0.020532755181193352,0.016100479289889336,0.004432275891304016,False,livecodebench
trace_livecodebench_53.jsonl,655,655,220,0.019216813147068024,0.017408769577741623,0.0018080435693264008,False,livecodebench
trace_livecodebench_54.jsonl,175,175,220,0.0350402370095253,0.015850862488150597,0.019189374521374702,True,livecodebench
trace_livecodebench_55.jsonl,61,61,1358,0.15963077545166016,0.13297712802886963,0.026653647422790527,True,livecodebench
trace_livecodebench_55.jsonl,580,580,279,0.3956615924835205,0.31099799275398254,0.08466359972953796,False,livecodebench
trace_livecodebench_55.jsonl,624,624,279,0.15994438529014587,0.15806853771209717,0.001875847578048706,True,livecodebench
trace_livecodebench_56.jsonl,68,68,482,0.08769623190164566,0.028590310364961624,0.059105921536684036,False,livecodebench
trace_livecodebench_56.jsonl,201,201,279,0.1190367341041565,0.06608609855175018,0.05295063555240631,False,livecodebench
trace_livecodebench_56.jsonl,399,399,3094,0.053239453583955765,0.0169391967356205,0.036300256848335266,False,livecodebench
trace_livecodebench_56.jsonl,446,446,220,0.06926627457141876,0.06442925333976746,0.004837021231651306,False,livecodebench
trace_livecodebench_56.jsonl,693,693,220,0.06080900877714157,0.03854767978191376,0.022261328995227814,False,livecodebench
trace_livecodebench_57.jsonl,90,90,279,0.28758007287979126,0.0838676244020462,0.20371244847774506,False,livecodebench
trace_livecodebench_57.jsonl,187,187,220,0.14960640668869019,0.12863436341285706,0.02097204327583313,False,livecodebench
trace_livecodebench_57.jsonl,225,225,11,0.3374958336353302,0.10938400775194168,0.22811182588338852,False,livecodebench
trace_livecodebench_57.jsonl,226,226,11,0.2001107931137085,0.05187157541513443,0.14823921769857407,True,livecodebench
trace_livecodebench_57.jsonl,229,229,220,0.03147856518626213,0.026338627561926842,0.005139937624335289,False,livecodebench
trace_livecodebench_57.jsonl,399,399,279,0.06569188088178635,0.04920703545212746,0.01648484542965889,True,livecodebench
trace_livecodebench_57.jsonl,624,624,279,0.5340425372123718,0.272318959236145,0.2617235779762268,True,livecodebench
trace_livecodebench_58.jsonl,35,35,311,0.022358087822794914,0.019045250490307808,0.0033128373324871063,True,livecodebench
trace_livecodebench_58.jsonl,124,124,311,0.24069301784038544,0.1822914481163025,0.05840156972408295,False,livecodebench
trace_livecodebench_58.jsonl,264,264,220,0.5555131435394287,0.5205694437026978,0.03494369983673096,False,livecodebench
trace_livecodebench_58.jsonl,329,329,220,0.6807422041893005,0.023471858352422714,0.6572703458368778,False,livecodebench
trace_livecodebench_58.jsonl,341,341,320,0.04120345041155815,0.030553339049220085,0.010650111362338066,False,livecodebench
trace_livecodebench_58.jsonl,350,350,602,0.01319429837167263,0.007877458818256855,0.005316839553415775,False,livecodebench
trace_livecodebench_58.jsonl,427,427,311,0.10242381691932678,0.08840902149677277,0.014014795422554016,False,livecodebench
trace_livecodebench_58.jsonl,444,444,311,0.03704897686839104,0.03699861094355583,5.036592483520508e-05,False,livecodebench
trace_livecodebench_58.jsonl,532,532,18,0.1620752215385437,0.023062871769070625,0.13901234976947308,False,livecodebench
trace_livecodebench_58.jsonl,666,666,11,0.023401066660881042,0.01268687378615141,0.010714192874729633,False,livecodebench
trace_livecodebench_59.jsonl,172,172,374,0.060718752443790436,0.02204976975917816,0.038668982684612274,False,livecodebench
trace_livecodebench_61.jsonl,329,329,279,0.3937569260597229,0.07924933731555939,0.3145075887441635,True,livecodebench
trace_livecodebench_61.jsonl,453,453,1855,0.2390957772731781,0.23066315054893494,0.008432626724243164,False,livecodebench
trace_livecodebench_61.jsonl,505,505,311,0.0907486155629158,0.04568718001246452,0.04506143555045128,False,livecodebench
trace_livecodebench_61.jsonl,643,643,279,0.36101558804512024,0.05436094105243683,0.3066546469926834,False,livecodebench
trace_livecodebench_62.jsonl,12,12,925,0.3182210624217987,0.3131312429904938,0.005089819431304932,True,livecodebench
trace_livecodebench_62.jsonl,17,17,1855,0.2049332559108734,0.11919993162155151,0.0857333242893219,True,livecodebench
trace_livecodebench_62.jsonl,99,99,370,0.987339437007904,0.2752600312232971,0.7120794057846069,True,livecodebench
trace_livecodebench_62.jsonl,208,208,311,0.20303143560886383,0.12178856879472733,0.0812428668141365,True,livecodebench
trace_livecodebench_62.jsonl,239,239,925,0.18624204397201538,0.1677708476781845,0.01847119629383087,True,livecodebench
trace_livecodebench_62.jsonl,313,313,374,0.12667065858840942,0.0608813650906086,0.06578929349780083,True,livecodebench
trace_livecodebench_63.jsonl,316,316,1855,0.13538885116577148,0.04622572660446167,0.08916312456130981,False,livecodebench
trace_livecodebench_63.jsonl,604,604,2082,0.3711227476596832,0.31252026557922363,0.058602482080459595,False,livecodebench
trace_livecodebench_64.jsonl,2,2,311,0.11968215554952621,0.07847918570041656,0.04120296984910965,False,livecodebench
trace_livecodebench_64.jsonl,95,95,311,0.059135179966688156,0.02445458620786667,0.03468059375882149,True,livecodebench
trace_livecodebench_64.jsonl,164,164,11,0.035893794149160385,0.03227075934410095,0.003623034805059433,True,livecodebench
trace_livecodebench_64.jsonl,212,212,374,0.03755097836256027,0.026805704459547997,0.010745273903012276,True,livecodebench
trace_livecodebench_64.jsonl,393,393,1523,0.034490715712308884,0.02333473041653633,0.011155985295772552,True,livecodebench
trace_livecodebench_64.jsonl,433,433,220,0.03687239810824394,0.015363184735178947,0.021509213373064995,False,livecodebench
trace_livecodebench_64.jsonl,693,693,489,0.43447816371917725,0.4305148720741272,0.003963291645050049,False,livecodebench
trace_livecodebench_65.jsonl,211,211,220,0.2957450747489929,0.07576808333396912,0.2199769914150238,False,livecodebench
trace_livecodebench_65.jsonl,216,216,220,0.4692726731300354,0.3935224413871765,0.07575023174285889,True,livecodebench
trace_livecodebench_65.jsonl,270,270,220,0.3435026705265045,0.25833046436309814,0.08517220616340637,False,livecodebench
trace_livecodebench_65.jsonl,559,559,3160,0.27963414788246155,0.11919993162155151,0.16043421626091003,True,livecodebench
trace_livecodebench_66.jsonl,174,174,220,0.15004435181617737,0.12989671528339386,0.02014763653278351,False,livecodebench
trace_livecodebench_66.jsonl,374,374,220,0.07997375726699829,0.019881438463926315,0.060092318803071976,True,livecodebench
trace_livecodebench_67.jsonl,54,54,311,0.18539515137672424,0.06871866434812546,0.11667648702859879,True,livecodebench
trace_livecodebench_67.jsonl,64,64,279,0.28238168358802795,0.24482133984565735,0.037560343742370605,False,livecodebench
trace_livecodebench_67.jsonl,356,356,311,0.43382301926612854,0.10685011744499207,0.3269729018211365,False,livecodebench
trace_livecodebench_68.jsonl,2,2,311,0.5347715020179749,0.47607138752937317,0.058700114488601685,False,livecodebench
trace_livecodebench_68.jsonl,5,5,311,0.09976286441087723,0.07847918570041656,0.021283678710460663,False,livecodebench
trace_livecodebench_68.jsonl,442,442,311,0.518410861492157,0.1377352476119995,0.38067561388015747,False,livecodebench
trace_livecodebench_68.jsonl,473,473,311,0.6331742405891418,0.39390695095062256,0.2392672896385193,False,livecodebench
trace_livecodebench_68.jsonl,489,489,279,0.35693421959877014,0.20099160075187683,0.1559426188468933,False,livecodebench
trace_livecodebench_68.jsonl,634,634,279,0.37740424275398254,0.37058377265930176,0.006820470094680786,False,livecodebench
trace_livecodebench_69.jsonl,74,74,311,0.4698401391506195,0.35970866680145264,0.11013147234916687,False,livecodebench
trace_livecodebench_69.jsonl,216,216,279,0.35076263546943665,0.1643652617931366,0.18639737367630005,False,livecodebench
trace_livecodebench_70.jsonl,350,350,1396,0.1280304491519928,0.0885818600654602,0.03944858908653259,False,livecodebench
trace_livecodebench_71.jsonl,53,53,311,0.0682833269238472,0.04787975549697876,0.02040357142686844,False,livecodebench
trace_livecodebench_71.jsonl,67,67,311,0.16566102206707,0.13693057000637054,0.028730452060699463,False,livecodebench
trace_livecodebench_71.jsonl,114,114,1988,0.16487446427345276,0.08980126678943634,0.07507319748401642,False,livecodebench
trace_livecodebench_71.jsonl,446,446,311,0.19581040740013123,0.06952870637178421,0.12628170102834702,False,livecodebench
trace_livecodebench_71.jsonl,473,473,11,0.2511846125125885,0.15485991537570953,0.09632469713687897,True,livecodebench
trace_livecodebench_72.jsonl,32,32,11,0.7011275291442871,0.26967254281044006,0.43145498633384705,False,livecodebench
trace_livecodebench_72.jsonl,490,490,311,0.3162984251976013,0.1281328648328781,0.1881655603647232,True,livecodebench
trace_livecodebench_72.jsonl,648,648,320,0.2768193781375885,0.2013845294713974,0.0754348486661911,True,livecodebench
trace_livecodebench_73.jsonl,436,436,11,0.13540486991405487,0.044891104102134705,0.09051376581192017,True,livecodebench
trace_livecodebench_73.jsonl,531,531,11,0.07476963102817535,0.04454176127910614,0.030227869749069214,False,livecodebench
trace_livecodebench_75.jsonl,68,68,11,0.12012680619955063,0.035930391401052475,0.08419641479849815,False,livecodebench
trace_livecodebench_77.jsonl,523,523,311,0.6087067723274231,0.48522406816482544,0.12348270416259766,False,livecodebench
trace_livecodebench_77.jsonl,567,567,311,0.49874478578567505,0.24244214594364166,0.2563026398420334,True,livecodebench
trace_livecodebench_78.jsonl,113,113,11,0.2844589352607727,0.2039574682712555,0.08050146698951721,False,livecodebench
trace_livecodebench_78.jsonl,694,694,1314,0.628998339176178,0.2188144475221634,0.4101838916540146,True,livecodebench
trace_livecodebench_79.jsonl,164,164,279,0.15869086980819702,0.04300304129719734,0.11568782851099968,True,livecodebench
trace_livecodebench_80.jsonl,35,35,311,0.7145136594772339,0.04568718001246452,0.6688264794647694,False,livecodebench
trace_livecodebench_80.jsonl,237,237,311,0.19640955328941345,0.04119439423084259,0.15521515905857086,False,livecodebench
trace_livecodebench_80.jsonl,378,378,489,0.25185903906822205,0.24196909368038177,0.009889945387840271,False,livecodebench
trace_livecodebench_81.jsonl,32,32,320,0.42629459500312805,0.2281985878944397,0.19809600710868835,False,livecodebench
trace_livecodebench_81.jsonl,61,61,220,0.46655645966529846,0.13693057000637054,0.3296258896589279,False,livecodebench
trace_livecodebench_81.jsonl,247,247,320,0.3681775629520416,0.30587759613990784,0.06229996681213379,False,livecodebench
trace_livecodebench_81.jsonl,342,342,320,0.6470116376876831,0.2717876136302948,0.3752240240573883,False,livecodebench
trace_livecodebench_81.jsonl,441,441,320,0.2293785810470581,0.20757435262203217,0.02180422842502594,False,livecodebench
trace_livecodebench_81.jsonl,454,454,11,0.06646057963371277,0.06595715135335922,0.0005034282803535461,False,livecodebench
trace_livecodebench_82.jsonl,327,327,382,0.06896865367889404,0.06518872827291489,0.0037799254059791565,False,livecodebench
trace_livecodebench_82.jsonl,432,432,311,0.1719191074371338,0.16040103137493134,0.011518076062202454,True,livecodebench
trace_livecodebench_83.jsonl,405,405,220,0.23826411366462708,0.14364221692085266,0.09462189674377441,False,livecodebench
trace_livecodebench_83.jsonl,412,412,279,0.2033347636461258,0.06858458369970322,0.13475017994642258,False,livecodebench
trace_livecodebench_83.jsonl,450,450,11,0.09011721611022949,0.03208222612738609,0.0580349899828434,False,livecodebench
trace_livecodebench_83.jsonl,455,455,220,0.4680725038051605,0.16711677610874176,0.30095572769641876,False,livecodebench
trace_livecodebench_84.jsonl,240,240,1176,0.6705726385116577,0.6015167832374573,0.06905585527420044,False,livecodebench
trace_livecodebench_84.jsonl,317,317,369,0.026981614530086517,0.01566619612276554,0.011315418407320976,True,livecodebench
trace_livecodebench_84.jsonl,339,339,364,0.3097259998321533,0.029497861862182617,0.2802281379699707,False,livecodebench
trace_livecodebench_84.jsonl,497,497,374,0.07739728689193726,0.024598296731710434,0.05279899016022682,False,livecodebench
trace_livecodebench_84.jsonl,504,504,1176,0.9684551358222961,0.7334040403366089,0.23505109548568726,False,livecodebench
trace_livecodebench_84.jsonl,579,579,304,0.03286883607506752,0.029729217290878296,0.0031396187841892242,False,livecodebench
trace_livecodebench_85.jsonl,3,3,311,0.2390460968017578,0.06557180732488632,0.1734742894768715,False,livecodebench
trace_livecodebench_85.jsonl,648,648,311,0.3292100429534912,0.12664006650447845,0.20256997644901276,False,livecodebench
trace_livecodebench_86.jsonl,439,439,220,0.6912456154823303,0.3224407434463501,0.3688048720359802,False,livecodebench
trace_livecodebench_86.jsonl,540,540,11,0.017834901809692383,0.01775212585926056,8.277595043182373e-05,False,livecodebench
trace_livecodebench_87.jsonl,773,773,220,0.09951010346412659,0.033621884882450104,0.06588821858167648,True,livecodebench
trace_livecodebench_88.jsonl,43,43,311,0.3554931879043579,0.06040758639574051,0.2950856015086174,False,livecodebench
trace_livecodebench_88.jsonl,68,68,6811,0.1486227810382843,0.1296432614326477,0.018979519605636597,True,livecodebench
trace_livecodebench_88.jsonl,144,144,6857,0.11026017367839813,0.06647446006536484,0.043785713613033295,True,livecodebench
trace_livecodebench_88.jsonl,372,372,11,0.17362602055072784,0.11666630208492279,0.056959718465805054,False,livecodebench
trace_livecodebench_89.jsonl,30,30,264,0.04706105589866638,0.019496897235512733,0.02756415866315365,False,livecodebench
trace_livecodebench_89.jsonl,38,38,264,0.10722976177930832,0.09157243371009827,0.015657328069210052,True,livecodebench
trace_livecodebench_89.jsonl,439,439,11,0.0463893823325634,0.04184310883283615,0.004546273499727249,False,livecodebench
trace_livecodebench_90.jsonl,266,266,304,0.4092904329299927,0.20001257956027985,0.20927785336971283,False,livecodebench
trace_livecodebench_90.jsonl,651,651,304,0.6199672818183899,0.260610967874527,0.3593563139438629,False,livecodebench
trace_livecodebench_91.jsonl,31,31,364,0.012536113150417805,0.009391325525939465,0.00314478762447834,False,livecodebench
trace_livecodebench_91.jsonl,92,92,489,0.3264084458351135,0.05310167372226715,0.2733067721128464,False,livecodebench
trace_livecodebench_91.jsonl,133,133,2694,0.04111941531300545,0.03953896462917328,0.0015804506838321686,True,livecodebench
trace_livecodebench_91.jsonl,199,199,315,0.2679206132888794,0.023655949160456657,0.24426466412842274,False,livecodebench
trace_livecodebench_91.jsonl,299,299,279,0.18956661224365234,0.10275676101446152,0.08680985122919083,False,livecodebench
trace_livecodebench_91.jsonl,331,331,279,0.052839137613773346,0.026753399521112442,0.026085738092660904,True,livecodebench
trace_livecodebench_91.jsonl,459,459,482,0.05072999745607376,0.049689922481775284,0.0010400749742984772,False,livecodebench
trace_livecodebench_91.jsonl,502,502,220,0.29520753026008606,0.18498140573501587,0.11022612452507019,False,livecodebench
trace_livecodebench_92.jsonl,317,317,326,0.28360840678215027,0.0851883515715599,0.19842005521059036,False,livecodebench
trace_livecodebench_92.jsonl,490,490,7677,0.02516627497971058,0.01674184948205948,0.0084244254976511,True,livecodebench
trace_livecodebench_92.jsonl,551,551,311,0.09532148391008377,0.035304319113492966,0.060017164796590805,False,livecodebench
trace_livecodebench_93.jsonl,314,314,11,0.2833483815193176,0.09085981547832489,0.19248856604099274,False,livecodebench
trace_livecodebench_93.jsonl,481,481,220,0.3184727728366852,0.192726269364357,0.12574650347232819,True,livecodebench
trace_livecodebench_93.jsonl,549,549,2694,0.4610518515110016,0.13349758088588715,0.32755427062511444,True,livecodebench
trace_livecodebench_93.jsonl,633,633,220,0.48717209696769714,0.4549364149570465,0.032235682010650635,False,livecodebench
trace_livecodebench_94.jsonl,10,10,13,0.20510032773017883,0.16420483589172363,0.0408954918384552,True,livecodebench
trace_livecodebench_94.jsonl,315,315,279,0.17029748857021332,0.04462883993983269,0.12566864863038063,False,livecodebench
trace_livecodebench_94.jsonl,467,467,279,0.26191675662994385,0.2065632939338684,0.05535346269607544,True,livecodebench
trace_livecodebench_95.jsonl,5,5,311,0.18843743205070496,0.15993180871009827,0.02850562334060669,False,livecodebench
trace_livecodebench_95.jsonl,149,149,1646,0.18333585560321808,0.10175815969705582,0.08157769590616226,False,livecodebench
trace_livecodebench_96.jsonl,268,268,279,0.39214441180229187,0.13746650516986847,0.2546779066324234,False,livecodebench
trace_livecodebench_96.jsonl,356,356,279,0.3482397198677063,0.33956900238990784,0.008670717477798462,False,livecodebench
trace_livecodebench_97.jsonl,115,115,311,0.6996235847473145,0.3586563467979431,0.34096723794937134,False,livecodebench
trace_livecodebench_97.jsonl,285,285,279,0.015290130861103535,0.010558951646089554,0.004731179215013981,False,livecodebench
trace_livecodebench_97.jsonl,366,366,28090,0.04090438783168793,0.0240284763276577,0.016875911504030228,True,livecodebench
trace_livecodebench_97.jsonl,372,372,18,0.014639130793511868,0.00892632920295,0.005712801590561867,False,livecodebench
trace_livecodebench_97.jsonl,518,518,11,0.048337172716856,0.029268307611346245,0.019068865105509758,True,livecodebench
trace_livecodebench_97.jsonl,663,663,1473,0.05372244119644165,0.027174705639481544,0.026547735556960106,True,livecodebench
trace_livecodebench_98.jsonl,118,118,279,0.13408592343330383,0.11530710011720657,0.01877882331609726,False,livecodebench
trace_livecodebench_98.jsonl,248,248,220,0.41806864738464355,0.12888585031032562,0.28918279707431793,True,livecodebench
trace_livecodebench_98.jsonl,627,627,11,0.07121424376964569,0.04300304129719734,0.02821120247244835,False,livecodebench
trace_livecodebench_99.jsonl,86,86,13,0.1732100546360016,0.11285623162984848,0.06035382300615311,False,livecodebench
trace_livecodebench_99.jsonl,217,217,13,0.10258232802152634,0.08112867921590805,0.021453648805618286,False,livecodebench
trace_livecodebench_99.jsonl,224,224,11,0.16054971516132355,0.13922280073165894,0.021326914429664612,False,livecodebench
trace_livecodebench_99.jsonl,245,245,11,0.07173829525709152,0.05958731845021248,0.012150976806879044,False,livecodebench
trace_livecodebench_99.jsonl,252,252,3868,0.052391327917575836,0.04143647477030754,0.010954853147268295,False,livecodebench
trace_livecodebench_99.jsonl,267,267,13,0.10144470632076263,0.04087381437420845,0.060570891946554184,False,livecodebench
trace_livecodebench_99.jsonl,274,274,13,0.30761224031448364,0.07503175735473633,0.23258048295974731,False,livecodebench
trace_livecodebench_99.jsonl,330,330,11,0.11653244495391846,0.0939272865653038,0.022605158388614655,False,livecodebench
trace_livecodebench_99.jsonl,337,337,11,0.09306707978248596,0.0797150507569313,0.013352029025554657,False,livecodebench
trace_livecodebench_99.jsonl,381,381,13,0.1520133912563324,0.10478345304727554,0.047229938209056854,False,livecodebench
trace_livecodebench_99.jsonl,385,385,3868,0.2318975031375885,0.13194230198860168,0.09995520114898682,True,livecodebench
trace_livecodebench_99.jsonl,412,412,11,0.19344112277030945,0.12107706069946289,0.07236406207084656,False,livecodebench
trace_livecodebench_99.jsonl,431,431,11,0.12987224757671356,0.08034025877714157,0.04953198879957199,False,livecodebench
trace_livecodebench_99.jsonl,442,442,3868,0.26536858081817627,0.07817322015762329,0.18719536066055298,False,livecodebench
trace_livecodebench_99.jsonl,467,467,3868,0.3861180245876312,0.16024447977542877,0.22587354481220245,True,livecodebench
trace_livecodebench_99.jsonl,469,469,11,0.162492036819458,0.11396373063325882,0.04852830618619919,False,livecodebench
trace_livecodebench_99.jsonl,498,498,3868,0.08839159458875656,0.07726247608661652,0.011129118502140045,False,livecodebench
trace_livecodebench_99.jsonl,503,503,3868,0.16585427522659302,0.06660442054271698,0.09924985468387604,False,livecodebench
trace_livecodebench_99.jsonl,549,549,3868,0.34097689390182495,0.10853276401758194,0.232444129884243,False,livecodebench
trace_livecodebench_99.jsonl,577,577,11,0.10608068108558655,0.09283299744129181,0.013247683644294739,True,livecodebench
trace_livecodebench_99.jsonl,605,605,3868,0.1967388242483139,0.14633232355117798,0.050406500697135925,False,livecodebench
trace_livecodebench_100.jsonl,46,46,13,0.1553487777709961,0.06269139051437378,0.09265738725662231,False,livecodebench
trace_livecodebench_100.jsonl,207,207,220,0.7887539267539978,0.547954797744751,0.24079912900924683,False,livecodebench
trace_livecodebench_100.jsonl,471,471,220,0.09258455038070679,0.03336023539304733,0.059224314987659454,False,livecodebench
trace_livecodebench_100.jsonl,519,519,11,0.023508351296186447,0.017891358584165573,0.005616992712020874,True,livecodebench
trace_livecodebench_100.jsonl,632,632,364,0.07627274841070175,0.06405284255743027,0.012219905853271484,False,livecodebench
trace_livecodebench_102.jsonl,453,453,220,0.39435887336730957,0.1041712835431099,0.2901875898241997,False,livecodebench
trace_livecodebench_102.jsonl,680,680,374,0.04723457992076874,0.045420266687870026,0.0018143132328987122,False,livecodebench
trace_livecodebench_102.jsonl,692,692,374,0.21562427282333374,0.0833776518702507,0.13224662095308304,False,livecodebench
trace_livecodebench_103.jsonl,1,1,11,0.05511920526623726,0.019765285775065422,0.03535391949117184,True,livecodebench
trace_livecodebench_103.jsonl,571,571,264,0.08832377940416336,0.06305979937314987,0.02526398003101349,False,livecodebench
trace_livecodebench_103.jsonl,593,593,279,0.1660218983888626,0.09193083643913269,0.07409106194972992,False,livecodebench
trace_livecodebench_104.jsonl,351,351,220,0.28622597455978394,0.10376516729593277,0.18246080726385117,False,livecodebench
trace_livecodebench_105.jsonl,105,105,11,0.04313943535089493,0.025829192250967026,0.017310243099927902,False,livecodebench
trace_livecodebench_106.jsonl,55,55,311,0.14453090727329254,0.05372761934995651,0.09080328792333603,False,livecodebench
trace_livecodebench_106.jsonl,307,307,311,0.34900039434432983,0.1108897477388382,0.23811064660549164,False,livecodebench
trace_livecodebench_106.jsonl,617,617,279,0.08449766039848328,0.07696125656366348,0.007536403834819794,False,livecodebench
trace_livecodebench_107.jsonl,22,22,11,0.025060763582587242,0.020713841542601585,0.004346922039985657,False,livecodebench
trace_livecodebench_107.jsonl,63,63,311,0.2509622871875763,0.0801834985613823,0.170778788626194,False,livecodebench
trace_livecodebench_107.jsonl,407,407,220,0.1504964679479599,0.12298373878002167,0.027512729167938232,True,livecodebench
trace_livecodebench_107.jsonl,451,451,1396,0.19702881574630737,0.17754775285720825,0.01948106288909912,False,livecodebench
trace_livecodebench_107.jsonl,596,596,220,0.5827897191047668,0.2938724756240845,0.2889172434806824,False,livecodebench
trace_livecodebench_108.jsonl,87,87,3044,0.48773378133773804,0.15993180871009827,0.32780197262763977,True,livecodebench
trace_livecodebench_108.jsonl,190,190,279,0.027058061212301254,0.02412252128124237,0.0029355399310588837,False,livecodebench
trace_livecodebench_109.jsonl,137,137,315,0.1711736023426056,0.16420483589172363,0.006968766450881958,False,livecodebench
trace_livecodebench_110.jsonl,31,31,279,0.09378834068775177,0.08452540636062622,0.00926293432712555,False,livecodebench
trace_livecodebench_110.jsonl,217,217,374,0.03035784140229225,0.013140829280018806,0.017217012122273445,False,livecodebench
trace_livecodebench_110.jsonl,320,320,279,0.15438243746757507,0.0846906527876854,0.06969178467988968,False,livecodebench
trace_livecodebench_111.jsonl,343,343,311,0.10058043152093887,0.08321495354175568,0.017365477979183197,False,livecodebench
trace_livecodebench_111.jsonl,525,525,961,0.21529531478881836,0.08208499848842621,0.13321031630039215,True,livecodebench
trace_livecodebench_112.jsonl,60,60,220,0.392193466424942,0.11575840413570404,0.276435062289238,True,livecodebench
trace_livecodebench_112.jsonl,344,344,11,0.03602639213204384,0.034486494958400726,0.0015398971736431122,False,livecodebench
trace_livecodebench_112.jsonl,361,361,220,0.4976097345352173,0.1946175992488861,0.3029921352863312,False,livecodebench
trace_livecodebench_114.jsonl,21,21,311,0.5914899110794067,0.39932936429977417,0.19216054677963257,True,livecodebench
trace_livecodebench_114.jsonl,58,58,279,0.26681891083717346,0.13428209722042084,0.13253681361675262,True,livecodebench
trace_livecodebench_114.jsonl,59,59,279,0.6806186437606812,0.6756434440612793,0.0049751996994018555,True,livecodebench
trace_livecodebench_114.jsonl,123,123,279,0.20850983262062073,0.17841681838035583,0.030093014240264893,True,livecodebench
trace_livecodebench_114.jsonl,343,343,13,0.026776734739542007,0.016354024410247803,0.010422710329294205,True,livecodebench
trace_livecodebench_114.jsonl,391,391,439,0.1857801079750061,0.15112492442131042,0.03465518355369568,True,livecodebench
trace_livecodebench_114.jsonl,407,407,382,0.053468577563762665,0.023153137415647507,0.030315440148115158,True,livecodebench
trace_livecodebench_114.jsonl,437,437,279,0.255935400724411,0.2175360769033432,0.03839932382106781,True,livecodebench
trace_livecodebench_115.jsonl,171,171,374,0.10730070620775223,0.0809703841805458,0.02633032202720642,False,livecodebench
trace_livecodebench_116.jsonl,195,195,1855,0.05116542428731918,0.047045473009347916,0.004119951277971268,True,livecodebench
trace_livecodebench_116.jsonl,394,394,10,0.12094196677207947,0.03923126682639122,0.08171069994568825,False,livecodebench
trace_livecodebench_116.jsonl,443,443,2479,0.06150747090578079,0.05126725137233734,0.010240219533443451,True,livecodebench
trace_livecodebench_117.jsonl,639,639,320,0.3737577497959137,0.24244214594364166,0.13131560385227203,False,livecodebench
trace_livecodebench_118.jsonl,102,102,605,0.14308659732341766,0.11485756188631058,0.028229035437107086,False,livecodebench
trace_livecodebench_119.jsonl,11,11,311,0.2256280928850174,0.19404825568199158,0.03157983720302582,False,livecodebench
trace_livecodebench_119.jsonl,23,23,2694,0.43002137541770935,0.38048499822616577,0.04953637719154358,True,livecodebench
trace_livecodebench_119.jsonl,88,88,5603,0.17630960047245026,0.15112492442131042,0.02518467605113983,True,livecodebench
trace_livecodebench_119.jsonl,413,413,2694,0.4130886197090149,0.18534304201602936,0.22774557769298553,False,livecodebench
trace_livecodebench_119.jsonl,552,552,2694,0.6677795648574829,0.5830100774765015,0.08476948738098145,False,livecodebench
trace_livecodebench_120.jsonl,163,163,5361,0.22828078269958496,0.06660442054271698,0.16167636215686798,False,livecodebench
trace_livecodebench_120.jsonl,527,527,374,0.02080785669386387,0.017138870432972908,0.0036689862608909607,False,livecodebench
trace_livecodebench_121.jsonl,1,1,11,0.11248186975717545,0.07786845415830612,0.034613415598869324,True,livecodebench
trace_livecodebench_121.jsonl,212,212,925,0.3776361644268036,0.22356639802455902,0.15406976640224457,True,livecodebench
trace_livecodebench_122.jsonl,48,48,99809,0.10566169768571854,0.06912250071763992,0.03653919696807861,True,livecodebench
trace_livecodebench_122.jsonl,401,401,2694,0.19132159650325775,0.09068252891302109,0.10063906759023666,False,livecodebench
trace_livecodebench_122.jsonl,505,505,311,0.15701542794704437,0.04143647477030754,0.11557895317673683,False,livecodebench
trace_livecodebench_122.jsonl,587,587,1473,0.2866944372653961,0.13117145001888275,0.15552298724651337,False,livecodebench
trace_livecodebench_123.jsonl,382,382,220,0.3229559063911438,0.06673462688922882,0.256221279501915,False,livecodebench
trace_livecodebench_124.jsonl,149,149,5540,0.2931379973888397,0.06858458369970322,0.2245534136891365,True,livecodebench
trace_livecodebench_125.jsonl,335,335,374,0.12676598131656647,0.07894036918878555,0.047825612127780914,True,livecodebench
trace_livecodebench_126.jsonl,421,421,11,0.11154986172914505,0.09671976417303085,0.014830097556114197,False,livecodebench
trace_livecodebench_127.jsonl,138,138,2766,0.4063384532928467,0.12664006650447845,0.2796983867883682,False,livecodebench
trace_livecodebench_127.jsonl,641,641,311,0.20429709553718567,0.1901092678308487,0.014187827706336975,False,livecodebench
trace_livecodebench_127.jsonl,695,695,320,0.08516353368759155,0.06417806446552277,0.020985469222068787,False,livecodebench
trace_livecodebench_128.jsonl,1,1,358,0.09728477895259857,0.07173578441143036,0.025548994541168213,True,livecodebench
trace_livecodebench_128.jsonl,379,379,311,0.07394383102655411,0.05446722358465195,0.01947660744190216,True,livecodebench
trace_livecodebench_129.jsonl,18,18,264,0.12555909156799316,0.07786845415830612,0.04769063740968704,False,livecodebench
trace_livecodebench_130.jsonl,248,248,596,0.36040404438972473,0.18246956169605255,0.17793448269367218,True,livecodebench
trace_livecodebench_130.jsonl,317,317,220,0.10909464955329895,0.09920698404312134,0.009887665510177612,True,livecodebench
trace_livecodebench_131.jsonl,29,29,279,0.5992173552513123,0.5720128417015076,0.027204513549804688,True,livecodebench
trace_livecodebench_131.jsonl,83,83,5540,0.011164161376655102,0.009502028115093708,0.0016621332615613937,True,livecodebench
trace_livecodebench_131.jsonl,123,123,279,0.5239579677581787,0.28594574332237244,0.23801222443580627,False,livecodebench
trace_livecodebench_131.jsonl,211,211,311,0.10345238447189331,0.04217129200696945,0.06128109246492386,False,livecodebench
trace_livecodebench_131.jsonl,271,271,311,0.26831379532814026,0.025728492066264153,0.2425853032618761,False,livecodebench
trace_livecodebench_131.jsonl,454,454,311,0.12255498021841049,0.06196100637316704,0.060593973845243454,False,livecodebench
trace_livecodebench_131.jsonl,574,574,279,0.035974808037281036,0.006063496228307486,0.02991131180897355,True,livecodebench
trace_livecodebench_131.jsonl,625,625,279,0.33550161123275757,0.10519356280565262,0.23030804842710495,False,livecodebench
trace_livecodebench_131.jsonl,626,626,279,0.8019932508468628,0.13719826936721802,0.6647949814796448,True,livecodebench
trace_livecodebench_132.jsonl,523,523,279,0.02758403867483139,0.017408769577741623,0.010175269097089767,False,livecodebench
trace_livecodebench_133.jsonl,151,151,364,0.04751766473054886,0.0169391967356205,0.03057846799492836,False,livecodebench
trace_livecodebench_133.jsonl,165,165,364,0.05120988190174103,0.026649096980690956,0.02456078492105007,False,livecodebench
trace_livecodebench_133.jsonl,169,169,220,0.2954658567905426,0.08720852434635162,0.20825733244419098,False,livecodebench
trace_livecodebench_134.jsonl,11,11,311,0.06469778716564178,0.03121686354279518,0.0334809236228466,False,livecodebench
trace_livecodebench_134.jsonl,31,31,323,0.18357664346694946,0.10789869725704193,0.07567794620990753,True,livecodebench
trace_livecodebench_134.jsonl,75,75,11,0.2096698135137558,0.1377352476119995,0.07193456590175629,True,livecodebench
trace_livecodebench_134.jsonl,338,338,311,0.045601312071084976,0.03678245469927788,0.008818857371807098,False,livecodebench
trace_livecodebench_134.jsonl,400,400,374,0.2065214216709137,0.09068252891302109,0.11583889275789261,False,livecodebench
trace_livecodebench_135.jsonl,472,472,304,0.6222798228263855,0.07415761798620224,0.5481222048401833,False,livecodebench
trace_livecodebench_136.jsonl,324,324,279,0.4580237865447998,0.44875890016555786,0.009264886379241943,False,livecodebench
trace_livecodebench_137.jsonl,73,73,220,0.17930017411708832,0.16875676810741425,0.010543406009674072,True,livecodebench
trace_livecodebench_137.jsonl,249,249,220,0.27790752053260803,0.10498830676078796,0.17291921377182007,False,livecodebench
trace_livecodebench_137.jsonl,468,468,11,0.053948719054460526,0.04462883993983269,0.009319879114627838,False,livecodebench
trace_livecodebench_137.jsonl,512,512,311,0.28681254386901855,0.17754775285720825,0.1092647910118103,True,livecodebench
trace_livecodebench_138.jsonl,340,340,279,0.380960613489151,0.1388155221939087,0.2421450912952423,True,livecodebench
trace_livecodebench_140.jsonl,141,141,311,0.1445305198431015,0.13194230198860168,0.012588217854499817,True,livecodebench
trace_livecodebench_141.jsonl,623,623,1314,0.4443492591381073,0.1281328648328781,0.3162163943052292,False,livecodebench
trace_livecodebench_142.jsonl,400,400,872,0.3423207402229309,0.25457391142845154,0.08774682879447937,True,livecodebench
trace_livecodebench_143.jsonl,195,195,11,0.034604694694280624,0.014432376250624657,0.020172318443655968,True,livecodebench
trace_livecodebench_143.jsonl,213,213,11,0.09895643591880798,0.03707094117999077,0.061885494738817215,False,livecodebench
trace_livecodebench_143.jsonl,314,314,11,0.042616866528987885,0.020273564383387566,0.02234330214560032,False,livecodebench
trace_livecodebench_143.jsonl,322,322,279,0.08635362237691879,0.06858458369970322,0.017769038677215576,True,livecodebench
trace_livecodebench_143.jsonl,372,372,220,0.6649407744407654,0.35413187742233276,0.3108088970184326,False,livecodebench
trace_livecodebench_144.jsonl,32,32,1566,0.32230764627456665,0.2445823848247528,0.07772526144981384,False,livecodebench
trace_livecodebench_144.jsonl,167,167,220,0.41449376940727234,0.3149714171886444,0.09952235221862793,False,livecodebench
trace_livecodebench_145.jsonl,189,189,279,0.09778770804405212,0.062082141637802124,0.03570556640625,False,livecodebench
trace_livecodebench_145.jsonl,433,433,343,0.271029531955719,0.24434363842010498,0.026685893535614014,True,livecodebench
trace_livecodebench_145.jsonl,515,515,279,0.32378122210502625,0.31558719277381897,0.008194029331207275,False,livecodebench
trace_livecodebench_146.jsonl,191,191,279,0.1825411319732666,0.09978997707366943,0.08275115489959717,False,livecodebench
trace_livecodebench_147.jsonl,42,42,374,0.09709896147251129,0.041517481207847595,0.055581480264663696,True,livecodebench
trace_livecodebench_147.jsonl,313,313,3321,0.584449291229248,0.24891969561576843,0.3355295956134796,False,livecodebench
trace_livecodebench_147.jsonl,420,420,3321,0.4561048448085785,0.44766464829444885,0.008440196514129639,True,livecodebench
trace_livecodebench_148.jsonl,51,51,311,0.08821678161621094,0.03103448450565338,0.057182297110557556,False,livecodebench
trace_livecodebench_148.jsonl,330,330,220,0.06323765963315964,0.031461700797080994,0.031775958836078644,False,livecodebench
trace_livecodebench_148.jsonl,331,331,220,0.28558316826820374,0.14921846985816956,0.13636469841003418,False,livecodebench
trace_livecodebench_149.jsonl,222,222,430,0.38904905319213867,0.16614042222499847,0.2229086309671402,True,livecodebench
trace_math500_0.jsonl,125,125,1486,0.04253854975104332,0.03103448450565338,0.011504065245389938,False,math500
trace_math500_0.jsonl,142,142,320,0.2091512233018875,0.04184310883283615,0.16730811446905136,False,math500
trace_math500_1.jsonl,446,446,311,0.035882242023944855,0.03115595318377018,0.004726288840174675,False,math500
trace_math500_4.jsonl,26,26,11,0.05431506782770157,0.019688228145241737,0.03462683968245983,True,math500
trace_math500_6.jsonl,796,796,374,0.27752214670181274,0.2035595029592514,0.07396264374256134,False,math500
trace_math500_7.jsonl,299,299,311,0.3331298232078552,0.2828904986381531,0.05023932456970215,False,math500
trace_math500_7.jsonl,334,334,220,0.2563384175300598,0.12939029932022095,0.12694811820983887,False,math500
trace_math500_7.jsonl,345,345,220,0.5133121609687805,0.4522785544395447,0.06103360652923584,False,math500
trace_math500_7.jsonl,570,570,220,0.4056341350078583,0.24267901480197906,0.1629551202058792,False,math500
trace_math500_8.jsonl,681,681,374,0.8481095433235168,0.34525343775749207,0.5028561055660248,False,math500
trace_math500_9.jsonl,40,40,220,0.7424112558364868,0.22909171879291534,0.5133195370435715,True,math500
trace_math500_9.jsonl,329,329,220,0.7478736042976379,0.21521176397800446,0.5326618403196335,False,math500
trace_math500_9.jsonl,369,369,220,0.26649391651153564,0.10275676101446152,0.16373715549707413,False,math500
trace_math500_9.jsonl,425,425,1912,0.2317928820848465,0.024075452238321304,0.2077174298465252,True,math500
trace_math500_9.jsonl,678,678,220,0.8716006278991699,0.24267901480197906,0.6289216130971909,False,math500
trace_math500_9.jsonl,681,681,220,0.260041207075119,0.2342955619096756,0.02574564516544342,False,math500
trace_math500_9.jsonl,699,699,220,0.813414454460144,0.4467911720275879,0.36662328243255615,True,math500
trace_math500_10.jsonl,193,193,220,0.3142988681793213,0.21479184925556183,0.09950701892375946,False,math500
trace_math500_10.jsonl,468,468,220,0.8989697098731995,0.40601420402526855,0.4929555058479309,False,math500
trace_math500_10.jsonl,574,574,721,0.7379739284515381,0.20616024732589722,0.5318136811256409,True,math500
trace_math500_10.jsonl,738,738,1980,0.5158852338790894,0.26575106382369995,0.2501341700553894,True,math500
trace_math500_10.jsonl,909,909,220,0.3593061864376068,0.2935856282711029,0.0657205581665039,False,math500
trace_math500_11.jsonl,175,175,220,0.39551058411598206,0.2181743085384369,0.17733627557754517,False,math500
trace_math500_11.jsonl,366,366,220,0.1569017618894577,0.07802069187164307,0.07888107001781464,False,math500
trace_math500_11.jsonl,559,559,220,0.4829491674900055,0.2525928020477295,0.230356365442276,False,math500
trace_math500_11.jsonl,656,656,220,0.3816165626049042,0.12060501426458359,0.2610115483403206,False,math500
trace_math500_11.jsonl,700,700,220,0.03010440059006214,0.019382990896701813,0.010721409693360329,False,math500
trace_math500_12.jsonl,39,39,220,0.5060296058654785,0.047045473009347916,0.4589841328561306,False,math500
trace_math500_12.jsonl,252,252,220,0.7019281387329102,0.11374136805534363,0.5881867706775665,False,math500
trace_math500_12.jsonl,322,322,220,0.6030294895172119,0.14733608067035675,0.45569340884685516,True,math500
trace_math500_12.jsonl,417,417,220,0.7896216511726379,0.14448635280132294,0.645135298371315,False,math500
trace_math500_13.jsonl,234,234,220,0.17955264449119568,0.17057935893535614,0.008973285555839539,False,math500
trace_math500_13.jsonl,299,299,220,0.5567348599433899,0.5347389578819275,0.021995902061462402,False,math500
trace_math500_14.jsonl,318,318,220,0.08579503744840622,0.0190080888569355,0.06678694859147072,False,math500
trace_math500_14.jsonl,621,621,220,0.6053280234336853,0.13402009010314941,0.4713079333305359,False,math500
trace_math500_16.jsonl,54,54,220,0.11884189397096634,0.05958731845021248,0.05925457552075386,False,math500
trace_math500_16.jsonl,55,55,220,0.6369187235832214,0.410198837518692,0.22671988606452942,False,math500
trace_math500_16.jsonl,64,64,374,0.04920652508735657,0.04308711737394333,0.0061194077134132385,False,math500
trace_math500_16.jsonl,114,114,220,0.12181217968463898,0.03544249385595322,0.08636968582868576,False,math500
trace_math500_16.jsonl,118,118,220,0.16426876187324524,0.1359977126121521,0.02827104926109314,False,math500
trace_math500_16.jsonl,151,151,11,0.029850702732801437,0.022749705240130424,0.007100997492671013,False,math500
trace_math500_16.jsonl,205,205,220,0.19022279977798462,0.12788285315036774,0.06233994662761688,False,math500
trace_math500_16.jsonl,356,356,220,0.6585748195648193,0.40226489305496216,0.2563099265098572,False,math500
trace_math500_16.jsonl,391,391,220,0.4654698967933655,0.20059941709041595,0.2648704797029495,False,math500
trace_math500_16.jsonl,430,430,311,0.33591148257255554,0.2049557864665985,0.13095569610595703,True,math500
trace_math500_16.jsonl,508,508,459,0.22390219569206238,0.025280185043811798,0.19862201064825058,False,math500
trace_math500_16.jsonl,573,573,220,0.529237687587738,0.49118348956108093,0.038054198026657104,False,math500
trace_math500_17.jsonl,138,138,6541,0.13864366710186005,0.04949619993567467,0.08914746716618538,True,math500
trace_math500_17.jsonl,233,233,220,0.06813902407884598,0.008255505003035069,0.05988351907581091,True,math500
trace_math500_17.jsonl,235,235,220,0.19148685038089752,0.019496897235512733,0.1719899531453848,False,math500
trace_math500_17.jsonl,305,305,220,0.25728341937065125,0.14519356191158295,0.1120898574590683,False,math500
trace_math500_17.jsonl,337,337,11,0.04709145054221153,0.028367817401885986,0.018723633140325546,False,math500
trace_math500_17.jsonl,417,417,220,0.4174760580062866,0.17174941301345825,0.24572664499282837,False,math500
trace_math500_17.jsonl,686,686,279,0.25456833839416504,0.251853883266449,0.0027144551277160645,False,math500
trace_math500_18.jsonl,201,201,320,0.1664387583732605,0.1532052755355835,0.013233482837677002,True,math500
trace_math500_19.jsonl,451,451,220,0.1302616149187088,0.08081239461898804,0.049449220299720764,False,math500
trace_math500_19.jsonl,711,711,220,0.14045266807079315,0.11827230453491211,0.022180363535881042,False,math500
trace_math500_19.jsonl,741,741,220,0.5262584686279297,0.4602990448474884,0.06595942378044128,False,math500
trace_math500_19.jsonl,767,767,220,0.6852713227272034,0.40979844331741333,0.27547287940979004,False,math500
trace_math500_21.jsonl,754,754,220,0.23811550438404083,0.023062871769070625,0.2150526326149702,False,math500
trace_math500_22.jsonl,165,165,220,0.07322050631046295,0.06699582189321518,0.006224684417247772,False,math500
trace_math500_22.jsonl,489,489,220,0.3430107533931732,0.10037640482187271,0.2426343485713005,True,math500
trace_math500_23.jsonl,8,8,220,0.29898327589035034,0.24410514533519745,0.05487813055515289,False,math500
trace_math500_23.jsonl,31,31,264,0.6217408180236816,0.2354423850774765,0.38629843294620514,True,math500
trace_math500_23.jsonl,97,97,220,0.4642904996871948,0.08049733191728592,0.3837931677699089,False,math500
trace_math500_23.jsonl,107,107,220,0.7037009000778198,0.3211836516857147,0.3825172483921051,False,math500
trace_math500_23.jsonl,108,108,220,0.5877784490585327,0.31435683369636536,0.27342161536216736,False,math500
trace_math500_23.jsonl,680,680,220,0.2561037540435791,0.13719826936721802,0.11890548467636108,False,math500
trace_math500_24.jsonl,490,490,489,0.6103103756904602,0.3551709055900574,0.25513947010040283,True,math500
trace_math500_24.jsonl,527,527,220,0.4320231080055237,0.07666121423244476,0.3553618937730789,False,math500
trace_math500_25.jsonl,86,86,24524,0.16658078134059906,0.16372446715831757,0.002856314182281494,False,math500
trace_math500_25.jsonl,154,154,220,0.0922217145562172,0.059355009347200394,0.0328667052090168,True,math500
trace_math500_25.jsonl,162,162,220,0.3076554536819458,0.30409058928489685,0.00356486439704895,False,math500
trace_math500_25.jsonl,241,241,220,0.3437493145465851,0.19652745127677917,0.1472218632698059,False,math500
trace_math500_25.jsonl,719,719,304,0.3448941111564636,0.33137911558151245,0.013514995574951172,False,math500
trace_math500_26.jsonl,276,276,220,0.03201651945710182,0.015125000849366188,0.016891518607735634,False,math500
trace_math500_26.jsonl,390,390,279,0.3905840218067169,0.2520999312400818,0.13848409056663513,True,math500
trace_math500_26.jsonl,471,471,220,0.11887479573488235,0.05238061025738716,0.0664941854774952,True,math500
trace_math500_28.jsonl,330,330,220,0.11899014562368393,0.11850352585315704,0.000486619770526886,False,math500
trace_math500_28.jsonl,363,363,510,0.1339578479528427,0.06256905943155289,0.07138878852128983,True,math500
trace_math500_29.jsonl,130,130,320,0.047073010355234146,0.04176146537065506,0.005311544984579086,False,math500
trace_math500_29.jsonl,332,332,220,0.5474656820297241,0.23636387288570404,0.3111018091440201,False,math500
trace_math500_29.jsonl,451,451,220,0.7297306656837463,0.13949498534202576,0.5902356803417206,False,math500
trace_math500_29.jsonl,495,495,220,0.40398937463760376,0.23752082884311676,0.166468545794487,False,math500
trace_math500_31.jsonl,113,113,279,0.038334500044584274,0.0190080888569355,0.019326411187648773,True,math500
trace_math500_31.jsonl,209,209,13,0.029658108949661255,0.027121679857373238,0.0025364290922880173,False,math500
trace_math500_32.jsonl,218,218,2015,0.13304102420806885,0.02685810998082161,0.10618291422724724,True,math500
trace_math500_32.jsonl,317,317,220,0.4355333745479584,0.25582000613212585,0.17971336841583252,False,math500
trace_math500_32.jsonl,790,790,311,0.035662729293107986,0.02932552807033062,0.006337201222777367,True,math500
trace_math500_33.jsonl,84,84,320,0.22432036697864532,0.021835487335920334,0.202484879642725,False,math500
trace_math500_33.jsonl,208,208,279,0.37381511926651,0.2667911648750305,0.10702395439147949,False,math500
trace_math500_33.jsonl,497,497,11,0.059414248913526535,0.03277894854545593,0.026635300368070602,True,math500
trace_math500_33.jsonl,499,499,220,0.07408113777637482,0.06725803762674332,0.0068231001496315,False,math500
trace_math500_33.jsonl,612,612,220,0.1624295860528946,0.06871866434812546,0.09371092170476913,False,math500
trace_math500_33.jsonl,680,680,220,0.2761407494544983,0.2535814046859741,0.02255934476852417,True,math500
trace_math500_33.jsonl,760,760,10,0.06704957783222198,0.03220779076218605,0.034841787070035934,False,math500
trace_math500_35.jsonl,35,35,358,0.3582579493522644,0.1722533255815506,0.1860046237707138,True,math500
trace_math500_35.jsonl,249,249,220,0.24517501890659332,0.1596197485923767,0.08555527031421661,False,math500
trace_math500_35.jsonl,414,414,220,0.284048855304718,0.12394831329584122,0.1601005420088768,False,math500
trace_math500_36.jsonl,118,118,220,0.25951460003852844,0.21353696286678314,0.0459776371717453,True,math500
trace_math500_36.jsonl,152,152,220,0.15701766312122345,0.11850352585315704,0.038514137268066406,True,math500
trace_math500_36.jsonl,211,211,220,0.3441260755062103,0.32307112216949463,0.021054953336715698,False,math500
trace_math500_36.jsonl,516,516,220,0.27164730429649353,0.25582000613212585,0.015827298164367676,False,math500
trace_math500_36.jsonl,628,628,15,0.289154976606369,0.22269479930400848,0.06646017730236053,False,math500
trace_math500_36.jsonl,631,631,374,0.10442950576543808,0.05741659924387932,0.04701290652155876,False,math500
trace_math500_37.jsonl,552,552,220,0.03445511683821678,0.031957149505615234,0.0024979673326015472,True,math500
trace_math500_39.jsonl,303,303,374,0.6939477920532227,0.6930180191993713,0.0009297728538513184,True,math500
trace_math500_39.jsonl,515,515,220,0.31707993149757385,0.2079801857471466,0.10909974575042725,False,math500
trace_math500_39.jsonl,609,609,220,0.31489723920822144,0.2071693390607834,0.10772790014743805,False,math500
trace_math500_39.jsonl,621,621,220,0.2799767553806305,0.16197513043880463,0.11800162494182587,False,math500
trace_math500_40.jsonl,256,256,220,0.07694714516401291,0.0608813650906086,0.016065780073404312,False,math500
trace_math500_41.jsonl,13,13,220,0.3652029037475586,0.24601967632770538,0.11918322741985321,False,math500
trace_math500_41.jsonl,99,99,3585,0.1768379807472229,0.16292698681354523,0.013910993933677673,True,math500
trace_math500_41.jsonl,152,152,220,0.23296542465686798,0.19576126337051392,0.037204161286354065,False,math500
trace_math500_41.jsonl,156,156,320,0.0876006931066513,0.07517845183610916,0.012422241270542145,False,math500
trace_math500_41.jsonl,304,304,220,0.9511668086051941,0.593059241771698,0.3581075668334961,False,math500
trace_math500_41.jsonl,318,318,220,0.5372079610824585,0.4087991714477539,0.1284087896347046,False,math500
trace_math500_41.jsonl,354,354,220,0.1318960338830948,0.08112867921590805,0.05076735466718674,True,math500
trace_math500_41.jsonl,416,416,220,0.5580461025238037,0.4058160185813904,0.15223008394241333,True,math500
trace_math500_41.jsonl,417,417,220,0.2649156153202057,0.25532084703445435,0.009594768285751343,True,math500
trace_math500_41.jsonl,632,632,220,0.864325761795044,0.22074608504772186,0.6435796767473221,False,math500
trace_math500_42.jsonl,199,199,220,0.08821827918291092,0.043851204216480255,0.044367074966430664,True,math500
trace_math500_43.jsonl,462,462,279,0.8006694912910461,0.3177519142627716,0.48291757702827454,False,math500
trace_math500_43.jsonl,512,512,220,0.5540167093276978,0.34156450629234314,0.21245220303535461,False,math500
trace_math500_43.jsonl,513,513,220,0.6390389800071716,0.2525928020477295,0.38644617795944214,True,math500
trace_math500_44.jsonl,184,184,220,0.3768545985221863,0.09766891598701477,0.2791856825351715,False,math500
trace_math500_44.jsonl,338,338,11,0.28866928815841675,0.02685810998082161,0.26181117817759514,True,math500
trace_math500_46.jsonl,58,58,311,0.04744803160429001,0.04008324444293976,0.00736478716135025,False,math500
trace_math500_46.jsonl,568,568,220,0.250519722700119,0.028814544901251793,0.22170517779886723,False,math500
trace_math500_47.jsonl,76,76,323,0.08468954265117645,0.02892732061445713,0.05576222203671932,True,math500
trace_math500_48.jsonl,59,59,220,0.4489668011665344,0.24529996514320374,0.2036668360233307,False,math500
trace_math500_48.jsonl,415,415,374,0.6649805903434753,0.5830100774765015,0.08197051286697388,False,math500
trace_math500_48.jsonl,436,436,220,0.18876902759075165,0.17394372820854187,0.014825299382209778,True,math500
trace_math500_49.jsonl,404,404,220,0.051014408469200134,0.044022832065820694,0.00699157640337944,True,math500
trace_math500_50.jsonl,68,68,11,0.19861838221549988,0.11575840413570404,0.08285997807979584,True,math500
trace_math500_50.jsonl,370,370,1047,0.13428056240081787,0.12131376564502716,0.01296679675579071,True,math500
trace_math500_50.jsonl,492,492,220,0.26071804761886597,0.09522026777267456,0.1654977798461914,False,math500
trace_math500_51.jsonl,213,213,220,0.4927074909210205,0.2181743085384369,0.2745331823825836,False,math500
trace_math500_51.jsonl,539,539,220,0.10873250663280487,0.04769309237599373,0.06103941425681114,False,math500
trace_math500_51.jsonl,692,692,220,0.09886769950389862,0.030913494527339935,0.06795420497655869,True,math500
trace_math500_51.jsonl,717,717,220,0.7394057512283325,0.307975709438324,0.43143004179000854,True,math500
trace_math500_52.jsonl,108,108,9518,0.0476277656853199,0.022661011666059494,0.024966754019260406,False,math500
trace_math500_52.jsonl,129,129,13,0.19776761531829834,0.03408471867442131,0.16368289664387703,True,math500
trace_math500_52.jsonl,181,181,13,0.2024834305047989,0.034486494958400726,0.16799693554639816,True,math500
trace_math500_52.jsonl,317,317,482,0.35287904739379883,0.06966463476419449,0.28321441262960434,True,math500
trace_math500_52.jsonl,358,358,220,0.03140094876289368,0.02892732061445713,0.0024736281484365463,False,math500
trace_math500_52.jsonl,507,507,220,0.14471730589866638,0.06939303874969482,0.07532426714897156,False,math500
trace_math500_52.jsonl,519,519,220,0.2905353605747223,0.22247743606567383,0.06805792450904846,False,math500
trace_math500_53.jsonl,156,156,11,0.17968812584877014,0.103360615670681,0.07632751017808914,False,math500
trace_math500_54.jsonl,494,494,220,0.12714609503746033,0.10853276401758194,0.018613331019878387,False,math500
trace_math500_54.jsonl,495,495,220,0.06452228873968124,0.02031319960951805,0.04420908913016319,False,math500
trace_math500_55.jsonl,254,254,220,0.28793689608573914,0.2407904863357544,0.04714640974998474,False,math500
trace_math500_55.jsonl,348,348,220,0.33575648069381714,0.31069445610046387,0.02506202459335327,False,math500
trace_math500_55.jsonl,495,495,489,0.06354635953903198,0.053518153727054596,0.010028205811977386,False,math500
trace_math500_56.jsonl,286,286,220,0.6215895414352417,0.10747803747653961,0.5141115039587021,False,math500
trace_math500_56.jsonl,331,331,220,0.7613969445228577,0.40800151228904724,0.3533954322338104,True,math500
trace_math500_56.jsonl,382,382,220,0.5552074909210205,0.503568708896637,0.051638782024383545,False,math500
trace_math500_56.jsonl,536,536,220,0.49461308121681213,0.26940929889678955,0.22520378232002258,False,math500
trace_math500_57.jsonl,220,220,220,0.28292834758758545,0.09882021695375443,0.18410813063383102,True,math500
trace_math500_58.jsonl,172,172,220,0.12917634844779968,0.12443342804908752,0.004742920398712158,False,math500
trace_math500_58.jsonl,215,215,220,0.35919973254203796,0.03085317462682724,0.3283465579152107,False,math500
trace_math500_58.jsonl,399,399,220,0.1628762036561966,0.08962604403495789,0.07325015962123871,False,math500
trace_math500_58.jsonl,421,421,279,0.11463607102632523,0.07802069187164307,0.03661537915468216,True,math500
trace_math500_58.jsonl,471,471,220,0.4784841537475586,0.44657301902770996,0.03191113471984863,False,math500
trace_math500_59.jsonl,460,460,220,0.23513220250606537,0.2057579606771469,0.029374241828918457,True,math500
trace_math500_60.jsonl,217,217,220,0.64150071144104,0.4721359610557556,0.16936475038528442,False,math500
trace_math500_60.jsonl,291,291,220,0.8163430690765381,0.5678386092185974,0.24850445985794067,False,math500
trace_math500_60.jsonl,357,357,220,0.3659071624279022,0.34898218512535095,0.01692497730255127,False,math500
trace_math500_60.jsonl,480,480,220,0.5542362928390503,0.14169171452522278,0.4125445783138275,False,math500
trace_math500_60.jsonl,485,485,220,0.5394775867462158,0.36217600107192993,0.1773015856742859,False,math500
trace_math500_60.jsonl,501,501,220,0.26031121611595154,0.18480083346366882,0.07551038265228271,False,math500
trace_math500_60.jsonl,640,640,220,0.37962231040000916,0.06885301321744919,0.31076929718255997,False,math500
trace_math500_61.jsonl,697,697,430,0.07449246197938919,0.060289718210697174,0.014202743768692017,True,math500
trace_math500_62.jsonl,47,47,279,0.4218911826610565,0.384782075881958,0.03710910677909851,False,math500
trace_math500_62.jsonl,801,801,374,0.25082507729530334,0.177374467253685,0.07345061004161835,False,math500
trace_math500_63.jsonl,95,95,11,0.2531430125236511,0.24244214594364166,0.01070086658000946,True,math500
trace_math500_66.jsonl,40,40,11,0.45043423771858215,0.03177044540643692,0.41866379231214523,False,math500
trace_math500_66.jsonl,79,79,220,0.14995358884334564,0.032144948840141296,0.11780864000320435,True,math500
trace_math500_66.jsonl,280,280,220,0.04127475246787071,0.026545202359557152,0.01472955010831356,False,math500
trace_math500_66.jsonl,436,436,220,0.36926132440567017,0.32496967911720276,0.04429164528846741,False,math500
trace_math500_66.jsonl,487,487,220,0.30932945013046265,0.19253815710544586,0.11679129302501678,False,math500
trace_math500_66.jsonl,611,611,220,0.3996555805206299,0.10705901682376862,0.29259656369686127,False,math500
trace_math500_66.jsonl,651,651,220,0.51811283826828,0.1666278839111328,0.3514849543571472,False,math500
trace_math500_66.jsonl,686,686,489,0.26756322383880615,0.22161005437374115,0.045953169465065,False,math500
trace_math500_67.jsonl,379,379,220,0.9544132947921753,0.8529471755027771,0.1014661192893982,False,math500
trace_math500_67.jsonl,408,408,220,0.6616801619529724,0.6543766260147095,0.0073035359382629395,False,math500
trace_math500_68.jsonl,590,590,220,0.2777556777000427,0.04334032163023949,0.23441535606980324,True,math500
trace_math500_68.jsonl,739,739,279,0.3106825649738312,0.28818845748901367,0.022494107484817505,True,math500
trace_math500_70.jsonl,51,51,279,0.11087405681610107,0.09015273302793503,0.020721323788166046,True,math500
trace_math500_70.jsonl,73,73,220,0.719408392906189,0.11873521655797958,0.6006731763482094,True,math500
trace_math500_70.jsonl,117,117,220,0.6547090411186218,0.6059386730194092,0.048770368099212646,False,math500
trace_math500_70.jsonl,120,120,220,0.15016642212867737,0.05468039959669113,0.09548602253198624,False,math500
trace_math500_70.jsonl,174,174,220,0.2629302442073822,0.13297712802886963,0.12995311617851257,True,math500
trace_math500_70.jsonl,320,320,304,0.32008278369903564,0.3017241060733795,0.018358677625656128,False,math500
trace_math500_71.jsonl,125,125,220,0.12876483798027039,0.05279143899679184,0.07597339898347855,False,math500
trace_math500_71.jsonl,361,361,220,0.43120500445365906,0.09690885990858078,0.3342961445450783,False,math500
trace_math500_71.jsonl,411,411,220,0.109367236495018,0.039616264402866364,0.06975097209215164,False,math500
trace_math500_71.jsonl,465,465,220,0.19424864649772644,0.17394372820854187,0.02030491828918457,True,math500
trace_math500_71.jsonl,533,533,220,0.7039787173271179,0.32624155282974243,0.3777371644973755,False,math500
trace_math500_71.jsonl,585,585,220,0.28698134422302246,0.23179219663143158,0.05518914759159088,False,math500
trace_math500_71.jsonl,641,641,220,0.15966875851154327,0.11873521655797958,0.04093354195356369,False,math500
trace_math500_71.jsonl,733,733,220,0.1639927625656128,0.042006880044937134,0.12198588252067566,True,math500
trace_math500_71.jsonl,736,736,220,0.880043089389801,0.7837600708007812,0.09628301858901978,False,math500
trace_math500_71.jsonl,741,741,220,0.3439473509788513,0.028478844091296196,0.3154685068875551,True,math500
trace_math500_71.jsonl,799,799,220,0.948887050151825,0.8679670691490173,0.08091998100280762,False,math500
trace_math500_71.jsonl,801,801,220,0.5781868696212769,0.5310959815979004,0.047090888023376465,False,math500
trace_math500_73.jsonl,182,182,220,0.6151898503303528,0.5642456412315369,0.05094420909881592,True,math500
trace_math500_73.jsonl,237,237,11,0.12234023213386536,0.03758125379681587,0.08475897833704948,False,math500
trace_math500_74.jsonl,101,101,1144,0.07804767787456512,0.02279418148100376,0.05525349639356136,False,math500
trace_math500_75.jsonl,75,75,2027,0.2552940845489502,0.10789869725704193,0.14739538729190826,True,math500
trace_math500_75.jsonl,170,170,220,0.3575984239578247,0.1155325323343277,0.242065891623497,False,math500
trace_math500_75.jsonl,184,184,220,0.4915836751461029,0.3520629405975342,0.13952073454856873,True,math500
trace_math500_75.jsonl,648,648,20124,0.5327169299125671,0.13976770639419556,0.3929492235183716,True,math500
trace_math500_75.jsonl,667,667,220,0.31073352694511414,0.08945116400718689,0.22128236293792725,False,math500
trace_math500_75.jsonl,674,674,220,0.17135871946811676,0.0205928273499012,0.15076589211821556,True,math500
trace_math500_77.jsonl,30,30,220,0.621061384677887,0.26549166440963745,0.3555697202682495,False,math500
trace_math500_78.jsonl,96,96,8,0.36824920773506165,0.11850352585315704,0.2497456818819046,False,math500
trace_math500_78.jsonl,624,624,220,0.17738889157772064,0.1710798293352127,0.006309062242507935,False,math500
trace_math500_80.jsonl,302,302,220,0.4130193591117859,0.12443342804908752,0.28858593106269836,True,math500
trace_math500_80.jsonl,470,470,220,0.14939579367637634,0.12763333320617676,0.021762460470199585,False,math500
trace_math500_82.jsonl,603,603,220,0.18155384063720703,0.16388444602489471,0.017669394612312317,False,math500
trace_math500_82.jsonl,717,717,220,0.05211357772350311,0.03586028143763542,0.01625329628586769,False,math500
trace_math500_83.jsonl,420,420,482,0.12118809670209885,0.08192483335733414,0.03926326334476471,True,math500
trace_math500_83.jsonl,710,710,220,0.19315266609191895,0.10664163529872894,0.08651103079319,False,math500
trace_math500_83.jsonl,719,719,16,0.03111565113067627,0.02204976975917816,0.009065881371498108,False,math500
trace_math500_84.jsonl,165,165,220,0.6900805234909058,0.32496967911720276,0.365110844373703,True,math500
trace_math500_84.jsonl,186,186,259,0.1077529639005661,0.04497886821627617,0.06277409568428993,False,math500
trace_math500_84.jsonl,361,361,220,0.3697204887866974,0.2848309576511383,0.08488953113555908,False,math500
trace_math500_84.jsonl,462,462,220,0.19498273730278015,0.1830049306154251,0.011977806687355042,False,math500
trace_math500_84.jsonl,518,518,220,0.4474170506000519,0.21166840195655823,0.23574864864349365,False,math500
trace_math500_84.jsonl,628,628,220,0.8905994892120361,0.8699824810028076,0.020617008209228516,True,math500
trace_math500_84.jsonl,639,639,220,0.4466775357723236,0.15068283677101135,0.29599469900131226,False,math500
trace_math500_85.jsonl,424,424,4478,0.5513994693756104,0.31527912616729736,0.236120343208313,True,math500
trace_math500_85.jsonl,546,546,220,0.16655907034873962,0.1126360148191452,0.05392305552959442,False,math500
trace_math500_87.jsonl,73,73,220,0.31839078664779663,0.25557029247283936,0.06282049417495728,True,math500
trace_math500_87.jsonl,294,294,220,0.4695076644420624,0.2834435701370239,0.18606409430503845,True,math500
trace_math500_87.jsonl,338,338,220,0.5447095036506653,0.2004036158323288,0.3443058878183365,False,math500
trace_math500_87.jsonl,457,457,220,0.2573985755443573,0.1296432614326477,0.1277553141117096,True,math500
trace_math500_88.jsonl,319,319,1584,0.06790058314800262,0.05310167372226715,0.014798909425735474,True,math500
trace_math500_88.jsonl,471,471,264,0.3964565396308899,0.14448635280132294,0.25197018682956696,True,math500
trace_math500_89.jsonl,98,98,220,0.22992727160453796,0.22074608504772186,0.009181186556816101,False,math500
trace_math500_89.jsonl,111,111,220,0.3526841402053833,0.2647149860858917,0.08796915411949158,False,math500
trace_math500_89.jsonl,163,163,220,0.6651601195335388,0.05958731845021248,0.6055728010833263,False,math500
trace_math500_89.jsonl,248,248,220,0.8632618188858032,0.3076750934123993,0.5555867254734039,False,math500
trace_math500_89.jsonl,359,359,220,0.3791659474372864,0.22204332053661346,0.1571226269006729,False,math500
trace_math500_89.jsonl,423,423,220,0.769727349281311,0.577908456325531,0.19181889295578003,False,math500
trace_math500_89.jsonl,480,480,220,0.5389601588249207,0.41992640495300293,0.11903375387191772,False,math500
trace_math500_90.jsonl,156,156,220,0.13253073394298553,0.014659653417766094,0.11787108052521944,True,math500
trace_math500_90.jsonl,213,213,13,0.1071852371096611,0.07847918570041656,0.028706051409244537,False,math500
trace_math500_90.jsonl,363,363,220,0.07820921391248703,0.06040758639574051,0.01780162751674652,True,math500
trace_math500_90.jsonl,658,658,50209,0.04200533777475357,0.021081171929836273,0.020924165844917297,True,math500
trace_math500_91.jsonl,400,400,11,0.06771062314510345,0.057641319930553436,0.010069303214550018,False,math500
trace_math500_91.jsonl,502,502,220,0.17158131301403046,0.1447688192129135,0.026812493801116943,False,math500
trace_math500_92.jsonl,92,92,356,0.021242080256342888,0.016807375475764275,0.004434704780578613,True,math500
trace_math500_92.jsonl,206,206,220,0.45684167742729187,0.11045743525028229,0.3463842421770096,False,math500
trace_math500_92.jsonl,337,337,220,0.23471252620220184,0.021920951083302498,0.21279157511889935,False,math500
trace_math500_92.jsonl,446,446,3487,0.06749066710472107,0.06699582189321518,0.0004948452115058899,True,math500
trace_math500_92.jsonl,448,448,220,0.4787531793117523,0.054043352603912354,0.42470982670783997,False,math500
trace_math500_92.jsonl,503,503,220,0.22477148473262787,0.11896734684705734,0.10580413788557053,False,math500
trace_math500_93.jsonl,22,22,279,0.7937428951263428,0.7375338077545166,0.05620908737182617,False,math500
trace_math500_94.jsonl,338,338,220,0.04109258949756622,0.028367817401885986,0.012724772095680237,False,math500
trace_math500_94.jsonl,614,614,11,0.02623542957007885,0.023471858352422714,0.0027635712176561356,True,math500
trace_math500_95.jsonl,14,14,482,0.2345484495162964,0.13854466378688812,0.09600378572940826,True,math500
trace_math500_95.jsonl,189,189,220,0.395862340927124,0.2593415379524231,0.13652080297470093,False,math500
trace_math500_95.jsonl,450,450,220,0.22453440725803375,0.20555713772773743,0.018977269530296326,False,math500
trace_math500_96.jsonl,234,234,220,0.36552831530570984,0.1806963086128235,0.18483200669288635,True,math500
trace_math500_96.jsonl,244,244,220,0.43967685103416443,0.31899556517601013,0.1206812858581543,False,math500
trace_math500_96.jsonl,264,264,220,0.3494012653827667,0.2618865668773651,0.08751469850540161,False,math500
trace_math500_96.jsonl,271,271,220,0.24284660816192627,0.18881411850452423,0.05403248965740204,False,math500
trace_math500_96.jsonl,397,397,220,0.6139650940895081,0.2102263867855072,0.40373870730400085,False,math500
trace_math500_96.jsonl,398,398,220,0.3662892282009125,0.15380489826202393,0.21248432993888855,True,math500
trace_math500_96.jsonl,399,399,220,0.44899314641952515,0.14420440793037415,0.304788738489151,False,math500
trace_math500_96.jsonl,402,402,220,0.2659529447555542,0.06818389892578125,0.19776904582977295,False,math500
trace_math500_96.jsonl,557,557,87,0.1704246550798416,0.1359977126121521,0.034426942467689514,False,math500
trace_math500_96.jsonl,762,762,220,0.18306340277194977,0.08962604403495789,0.09343735873699188,True,math500
trace_math500_98.jsonl,88,88,311,0.7738518118858337,0.028702208772301674,0.7451496031135321,True,math500
trace_math500_99.jsonl,347,347,320,0.1994265764951706,0.1526079922914505,0.04681858420372009,False,math500
trace_math500_100.jsonl,33,33,435,0.13191473484039307,0.10622588545084,0.02568884938955307,False,math500
trace_math500_100.jsonl,128,128,311,0.08439476042985916,0.037876006215810776,0.046518754214048386,True,math500
trace_math500_100.jsonl,326,326,220,0.19357791543006897,0.17824265360832214,0.015335261821746826,False,math500
trace_math500_101.jsonl,120,120,304,0.2450229525566101,0.1978754997253418,0.04714745283126831,False,math500
trace_math500_101.jsonl,311,311,220,0.45804667472839355,0.23567241430282593,0.22237426042556763,False,math500
trace_math500_101.jsonl,345,345,220,0.4679611325263977,0.06392785906791687,0.40403327345848083,False,math500
trace_math500_101.jsonl,362,362,220,0.07504624128341675,0.04008324444293976,0.03496299684047699,True,math500
trace_math500_101.jsonl,503,503,220,0.14636562764644623,0.13402009010314941,0.012345537543296814,False,math500
trace_math500_101.jsonl,536,536,311,0.37378990650177,0.2513624429702759,0.12242746353149414,True,math500
trace_math500_102.jsonl,14,14,11,0.41071173548698425,0.09229064732789993,0.3184210881590843,False,math500
trace_math500_102.jsonl,33,33,311,0.16772057116031647,0.05289464816451073,0.11482592299580574,False,math500
trace_math500_102.jsonl,144,144,220,0.1598849594593048,0.15501122176647186,0.004873737692832947,False,math500
trace_math500_102.jsonl,333,333,220,0.3806426525115967,0.3653732240200043,0.015269428491592407,False,math500
trace_math500_103.jsonl,414,414,865,0.35126280784606934,0.2834435701370239,0.06781923770904541,False,math500
trace_math500_104.jsonl,395,395,220,0.21625672280788422,0.07924933731555939,0.13700738549232483,True,math500
trace_math500_104.jsonl,531,531,220,0.24118201434612274,0.23452448844909668,0.006657525897026062,True,math500
trace_math500_104.jsonl,555,555,220,0.8844989538192749,0.27579817175865173,0.6087007820606232,False,math500
trace_math500_104.jsonl,606,606,220,0.861789882183075,0.5587621927261353,0.3030276894569397,False,math500
trace_math500_104.jsonl,622,622,220,0.3453879952430725,0.19981735944747925,0.14557063579559326,False,math500
trace_math500_104.jsonl,713,713,220,0.5135285258293152,0.2595949172973633,0.2539336085319519,False,math500
trace_math500_105.jsonl,160,160,279,0.18875722587108612,0.12298373878002167,0.06577348709106445,True,math500
trace_math500_105.jsonl,240,240,220,0.3110370635986328,0.07532542943954468,0.23571163415908813,False,math500
trace_math500_109.jsonl,585,585,220,0.5194257497787476,0.11024190485477448,0.4091838449239731,False,math500
trace_math500_109.jsonl,600,600,220,0.29733583331108093,0.06582845747470856,0.23150737583637238,False,math500
trace_math500_110.jsonl,89,89,353,0.13313333690166473,0.04649737849831581,0.08663595840334892,False,math500
trace_math500_110.jsonl,288,288,961,0.331398069858551,0.18844570219516754,0.14295236766338348,True,math500
trace_math500_110.jsonl,481,481,220,0.2036561369895935,0.026649096980690956,0.17700704000890255,False,math500
trace_math500_110.jsonl,485,485,220,0.14080335199832916,0.08703836053609848,0.05376499146223068,False,math500
trace_math500_111.jsonl,195,195,220,0.2860601842403412,0.04225373640656471,0.24380644783377647,False,math500
trace_math500_111.jsonl,196,196,220,0.14132407307624817,0.017821604385972023,0.12350246869027615,True,math500
trace_math500_111.jsonl,309,309,220,0.25663429498672485,0.06147882342338562,0.19515547156333923,True,math500
trace_math500_111.jsonl,334,334,220,0.06202145293354988,0.03290724381804466,0.02911420911550522,True,math500
trace_math500_111.jsonl,340,340,220,0.24869105219841003,0.06621529906988144,0.1824757531285286,False,math500
trace_math500_111.jsonl,470,470,220,0.019519509747624397,0.01824423298239708,0.0012752767652273178,False,math500
trace_math500_111.jsonl,517,517,220,0.25850462913513184,0.05289464816451073,0.2056099809706211,False,math500
trace_math500_112.jsonl,62,62,315,0.014667988754808903,0.01239298190921545,0.0022750068455934525,True,math500
trace_math500_112.jsonl,466,466,11,0.11112610250711441,0.06752128154039383,0.04360482096672058,True,math500
trace_math500_112.jsonl,571,571,311,0.09778723865747452,0.05820697546005249,0.03958026319742203,True,math500
trace_math500_112.jsonl,593,593,11,0.09368643164634705,0.026031771674752235,0.06765465997159481,True,math500
trace_math500_113.jsonl,54,54,374,0.6849174499511719,0.376787394285202,0.30813005566596985,False,math500
trace_math500_113.jsonl,160,160,220,0.4619390070438385,0.3520629405975342,0.10987606644630432,False,math500
trace_math500_114.jsonl,470,470,220,0.623911440372467,0.0747392401099205,0.5491722002625465,False,math500
trace_math500_114.jsonl,471,471,220,0.7629089951515198,0.09301448613405228,0.6698945090174675,False,math500
trace_math500_114.jsonl,535,535,220,0.25980037450790405,0.13349758088588715,0.1263027936220169,False,math500
trace_math500_114.jsonl,547,547,220,0.7425965666770935,0.16008806228637695,0.5825085043907166,False,math500
trace_math500_115.jsonl,40,40,11,0.43358004093170166,0.13428209722042084,0.2992979437112808,False,math500
trace_math500_115.jsonl,56,56,11,0.16351915895938873,0.042585138231515884,0.12093402072787285,False,math500
trace_math500_115.jsonl,118,118,220,0.022319816052913666,0.018495379015803337,0.0038244370371103287,False,math500
trace_math500_115.jsonl,168,168,220,0.50932776927948,0.4332563281059265,0.07607144117355347,False,math500
trace_math500_115.jsonl,169,169,220,0.28989505767822266,0.21002118289470673,0.07987387478351593,False,math500
trace_math500_115.jsonl,332,332,220,0.12310668081045151,0.08997683227062225,0.033129848539829254,False,math500
trace_math500_115.jsonl,363,363,220,0.03359813243150711,0.01882336661219597,0.014774765819311142,True,math500
trace_math500_115.jsonl,406,406,220,0.11785829067230225,0.040240127593278885,0.07761816307902336,False,math500
trace_math500_115.jsonl,469,469,13,0.08849784731864929,0.06305979937314987,0.02543804794549942,True,math500
trace_math500_115.jsonl,495,495,220,0.368225634098053,0.03900206834077835,0.3292235657572746,False,math500
trace_math500_115.jsonl,612,612,220,0.21198101341724396,0.0346214696764946,0.17735954374074936,True,math500
trace_math500_115.jsonl,700,700,220,0.29429611563682556,0.26862120628356934,0.025674909353256226,False,math500
trace_math500_115.jsonl,701,701,220,0.34854206442832947,0.023655949160456657,0.3248861152678728,False,math500
trace_math500_116.jsonl,92,92,279,0.040816780179739,0.020115792751312256,0.020700987428426743,False,math500
trace_math500_116.jsonl,519,519,4320,0.042315855622291565,0.023609790951013565,0.018706064671278,True,math500
trace_math500_117.jsonl,18,18,358,0.9418655037879944,0.8066674470901489,0.13519805669784546,True,math500
trace_math500_118.jsonl,47,47,220,0.11587489396333694,0.10356269031763077,0.012312203645706177,False,math500
trace_math500_118.jsonl,243,243,220,0.3389163911342621,0.2535814046859741,0.08533498644828796,True,math500
trace_math500_118.jsonl,387,387,374,0.05247918888926506,0.03877420723438263,0.013704981654882431,False,math500
trace_math500_118.jsonl,599,599,220,0.3744223415851593,0.32433557510375977,0.050086766481399536,False,math500
trace_math500_118.jsonl,692,692,279,0.24398298561573029,0.1789402961730957,0.06504268944263458,True,math500
trace_math500_119.jsonl,21,21,220,0.18239495158195496,0.0868685320019722,0.09552641957998276,True,math500
trace_math500_119.jsonl,25,25,220,0.1786353886127472,0.06725803762674332,0.11137735098600388,True,math500
trace_math500_119.jsonl,58,58,220,0.5974672436714172,0.10832099616527557,0.48914624750614166,False,math500
trace_math500_119.jsonl,131,131,220,0.2697286605834961,0.23636387288570404,0.03336478769779205,True,math500
trace_math500_119.jsonl,189,189,220,0.19240884482860565,0.09596709161996841,0.09644175320863724,True,math500
trace_math500_119.jsonl,340,340,220,0.6678109765052795,0.5119984745979309,0.15581250190734863,False,math500
trace_math500_119.jsonl,365,365,220,0.3712579905986786,0.1902950257062912,0.1809629648923874,True,math500
trace_math500_119.jsonl,393,393,220,0.8084838390350342,0.2964667081832886,0.5120171308517456,True,math500
trace_math500_119.jsonl,398,398,220,0.31686869263648987,0.11689439415931702,0.19997429847717285,False,math500
trace_math500_119.jsonl,516,516,220,0.5461843609809875,0.5218418836593628,0.024342477321624756,True,math500
trace_math500_121.jsonl,45,45,220,0.09555760025978088,0.0868685320019722,0.008689068257808685,False,math500
trace_math500_121.jsonl,129,129,24524,0.17883992195129395,0.07909470051527023,0.09974522143602371,True,math500
trace_math500_122.jsonl,93,93,11,0.09326837956905365,0.02825722098350525,0.0650111585855484,True,math500
trace_math500_123.jsonl,63,63,320,0.19488079845905304,0.060172077268362045,0.134708721190691,False,math500
trace_math500_123.jsonl,92,92,320,0.4403407573699951,0.28959909081459045,0.15074166655540466,False,math500
trace_math500_123.jsonl,271,271,24524,0.0993957668542862,0.07606463134288788,0.023331135511398315,True,math500
trace_math500_123.jsonl,388,388,489,0.4407707452774048,0.10581174492835999,0.3349590003490448,False,math500
trace_math500_123.jsonl,590,590,2015,0.3632229268550873,0.27338477969169617,0.08983814716339111,True,math500
trace_math500_123.jsonl,684,684,220,0.048648204654455185,0.03246040269732475,0.016187801957130432,False,math500
trace_math500_124.jsonl,633,633,220,0.21246333420276642,0.09015273302793503,0.12231060117483139,True,math500
trace_math500_125.jsonl,26,26,13,0.04000016301870346,0.022528620436787605,0.017471542581915855,False,math500
trace_math500_125.jsonl,36,36,220,0.45806682109832764,0.2755289673805237,0.18253785371780396,False,math500
trace_math500_125.jsonl,123,123,25,0.11631136387586594,0.09374400973320007,0.022567354142665863,True,math500
trace_math500_125.jsonl,157,157,13,0.04480687901377678,0.01283642090857029,0.03197045810520649,False,math500
trace_math500_125.jsonl,232,232,13,0.04492001608014107,0.031957149505615234,0.012962866574525833,False,math500
trace_math500_125.jsonl,285,285,11,0.5658214092254639,0.21353696286678314,0.3522844463586807,False,math500
trace_math500_127.jsonl,123,123,220,0.3190387189388275,0.1643652617931366,0.15467345714569092,False,math500
trace_math500_127.jsonl,179,179,220,0.04483992978930473,0.03877420723438263,0.006065722554922104,False,math500
trace_math500_127.jsonl,293,293,374,0.02009943686425686,0.017340898513793945,0.0027585383504629135,True,math500
trace_math500_127.jsonl,351,351,220,0.27485141158103943,0.02175035886466503,0.2531010527163744,False,math500
trace_math500_127.jsonl,374,374,374,0.04907526820898056,0.010936766862869263,0.0381385013461113,True,math500
trace_math500_127.jsonl,387,387,220,0.5232009887695312,0.37623587250709534,0.1469651162624359,False,math500
trace_math500_127.jsonl,525,525,220,0.3964628279209137,0.10076926648616791,0.2956935614347458,True,math500
trace_math500_127.jsonl,527,527,220,0.4135423004627228,0.24244214594364166,0.17110015451908112,False,math500
trace_math500_127.jsonl,543,543,220,0.2518269419670105,0.14576184749603271,0.10606509447097778,False,math500
trace_math500_127.jsonl,575,575,220,0.6182408332824707,0.15275710821151733,0.46548372507095337,False,math500
trace_math500_128.jsonl,41,41,264,0.10569488257169724,0.0067379469983279705,0.09895693557336926,True,math500
trace_math500_128.jsonl,455,455,11,0.42098352313041687,0.021455014124512672,0.3995285090059042,False,math500
trace_math500_128.jsonl,464,464,220,0.11242733895778656,0.03642499819397926,0.0760023407638073,False,math500
trace_math500_128.jsonl,613,613,220,0.33355608582496643,0.08772101998329163,0.2458350658416748,True,math500
trace_math500_129.jsonl,386,386,220,0.016761714592576027,0.008719551376998425,0.008042163215577602,True,math500
trace_math500_130.jsonl,181,181,374,0.2750856280326843,0.26627060770988464,0.008815020322799683,False,math500
trace_math500_130.jsonl,346,346,358,0.19532285630702972,0.14210744202136993,0.05321541428565979,False,math500
trace_math500_130.jsonl,561,561,220,0.5644757151603699,0.18193577229976654,0.38253994286060333,False,math500
trace_math500_132.jsonl,101,101,220,0.29448336362838745,0.27311792969703674,0.021365433931350708,False,math500
trace_math500_132.jsonl,125,125,220,0.28467461466789246,0.10215643048286438,0.18251818418502808,False,math500
trace_math500_132.jsonl,140,140,11,0.21214397251605988,0.010234087705612183,0.2019098848104477,False,math500
trace_math500_132.jsonl,157,157,220,0.19067105650901794,0.1025562584400177,0.08811479806900024,False,math500
trace_math500_132.jsonl,183,183,11,0.03687897324562073,0.014376109465956688,0.02250286377966404,False,math500
trace_math500_132.jsonl,217,217,220,0.12892572581768036,0.02831246517598629,0.10061326064169407,True,math500
trace_math500_132.jsonl,308,308,220,0.3779236376285553,0.08144620805978775,0.29647742956876755,False,math500
trace_math500_132.jsonl,312,312,1160,0.07571582496166229,0.07090003043413162,0.00481579452753067,False,math500
trace_math500_134.jsonl,432,432,220,0.06068297475576401,0.05468039959669113,0.006002575159072876,False,math500
trace_math500_134.jsonl,468,468,220,0.06866933405399323,0.04454176127910614,0.024127572774887085,False,math500
trace_math500_135.jsonl,537,537,311,0.4752366840839386,0.33824512362480164,0.13699156045913696,True,math500
trace_math500_136.jsonl,180,180,757,0.5584975481033325,0.2079801857471466,0.3505173623561859,False,math500
trace_math500_136.jsonl,447,447,220,0.4845688045024872,0.3412310779094696,0.14333772659301758,True,math500
trace_math500_137.jsonl,29,29,220,0.2403278648853302,0.21668799221515656,0.023639872670173645,False,math500
trace_math500_137.jsonl,127,127,220,0.1304321438074112,0.05279143899679184,0.07764070481061935,True,math500
trace_math500_138.jsonl,141,141,11,0.1365329921245575,0.061599016189575195,0.0749339759349823,False,math500
trace_math500_138.jsonl,223,223,11,0.09552232176065445,0.018031680956482887,0.07749064080417156,True,math500
trace_math500_138.jsonl,328,328,220,0.32291001081466675,0.0931963324546814,0.22971367835998535,False,math500
trace_math500_138.jsonl,329,329,220,0.6315311789512634,0.06557180732488632,0.5659593716263771,True,math500
trace_math500_138.jsonl,551,551,220,0.5258163809776306,0.22204332053661346,0.30377306044101715,True,math500
trace_math500_138.jsonl,553,553,220,0.10901207476854324,0.056416142731904984,0.05259593203663826,False,math500
trace_math500_139.jsonl,278,278,17,0.16288144886493683,0.10981211811304092,0.053069330751895905,False,math500
trace_math500_140.jsonl,184,184,220,0.41727957129478455,0.3989395797252655,0.018339991569519043,False,math500
trace_math500_141.jsonl,6,6,311,0.19043201208114624,0.046953678131103516,0.14347833395004272,True,math500
trace_math500_141.jsonl,467,467,439,0.23841975629329681,0.027710678055882454,0.21070907823741436,False,math500
trace_math500_142.jsonl,688,688,220,0.4978019893169403,0.3459284007549286,0.15187358856201172,False,math500
trace_math500_142.jsonl,808,808,16,0.4880277216434479,0.45073533058166504,0.03729239106178284,False,math500
trace_math500_143.jsonl,156,156,220,0.33902207016944885,0.21626517176628113,0.12275689840316772,True,math500
trace_math500_143.jsonl,198,198,220,0.6613348722457886,0.23752082884311676,0.4238140434026718,False,math500
trace_math500_143.jsonl,269,269,220,0.06332577764987946,0.04055573418736458,0.022770043462514877,False,math500
trace_math500_143.jsonl,341,341,220,0.6825473308563232,0.18516212701797485,0.4973852038383484,True,math500
trace_math500_143.jsonl,379,379,220,0.6333579421043396,0.08806435018777847,0.5452935919165611,False,math500
trace_math500_143.jsonl,448,448,91,0.03634802997112274,0.0325874462723732,0.0037605836987495422,False,math500
trace_math500_143.jsonl,474,474,220,0.33717575669288635,0.04143647477030754,0.2957392819225788,True,math500
trace_math500_144.jsonl,167,167,482,0.11518581956624985,0.022484663873910904,0.09270115569233894,False,math500
trace_math500_145.jsonl,487,487,220,0.26330703496932983,0.17513687908649445,0.08817015588283539,True,math500
trace_math500_145.jsonl,531,531,220,0.5109663605690002,0.2481914907693863,0.26277486979961395,True,math500
trace_math500_146.jsonl,1,1,11,0.08313611149787903,0.02803732082247734,0.05509879067540169,True,math500
trace_math500_146.jsonl,206,206,220,0.09677431732416153,0.039154719561338425,0.057619597762823105,True,math500
trace_math500_146.jsonl,315,315,323,0.13133765757083893,0.06845075637102127,0.06288690119981766,True,math500
trace_math500_146.jsonl,351,351,220,0.10782254487276077,0.045776501297950745,0.06204604357481003,False,math500
trace_math500_146.jsonl,418,418,20,0.0540207177400589,0.023517746478319168,0.03050297126173973,True,math500
trace_math500_146.jsonl,577,577,220,0.19276253879070282,0.09671976417303085,0.09604277461767197,False,math500
trace_math500_146.jsonl,621,621,220,0.18640007078647614,0.1677708476781845,0.018629223108291626,False,math500
trace_math500_147.jsonl,810,810,220,0.30387693643569946,0.272318959236145,0.03155797719955444,False,math500
trace_math500_148.jsonl,25,25,311,0.08921030163764954,0.019959252327680588,0.06925104930996895,False,math500
trace_math500_148.jsonl,253,253,11,0.020352762192487717,0.01856776885688305,0.0017849933356046677,True,math500
trace_math500_148.jsonl,378,378,1035,0.03512950614094734,0.03435204178094864,0.000777464359998703,False,math500
trace_math500_149.jsonl,315,315,220,0.2617678940296173,0.23021307587623596,0.03155481815338135,False,math500
trace_math500_150.jsonl,134,134,220,0.11251845210790634,0.0724397599697113,0.04007869213819504,True,math500
trace_math500_150.jsonl,415,415,11,0.1238374188542366,0.0939272865653038,0.0299101322889328,True,math500
trace_math500_150.jsonl,618,618,220,0.18485818803310394,0.03892596811056137,0.14593221992254257,True,math500
trace_math500_151.jsonl,113,113,11,0.2836291790008545,0.08703836053609848,0.196590818464756,False,math500
trace_math500_152.jsonl,612,612,1486,0.21496963500976562,0.06871866434812546,0.14625097066164017,False,math500
trace_math500_152.jsonl,640,640,220,0.09227621555328369,0.04462883993983269,0.047647375613451004,False,math500
trace_math500_152.jsonl,673,673,320,0.14035555720329285,0.027015943080186844,0.113339614123106,True,math500
trace_math500_153.jsonl,662,662,17,0.1715126633644104,0.059355009347200394,0.11215765401721,True,math500
trace_math500_153.jsonl,663,663,323,0.04538363590836525,0.031584836542606354,0.013798799365758896,False,math500
trace_math500_154.jsonl,221,221,13,0.09051641821861267,0.05597710609436035,0.03453931212425232,False,math500
trace_math500_154.jsonl,303,303,220,0.24498587846755981,0.14238525927066803,0.10260061919689178,False,math500
trace_math500_155.jsonl,92,92,220,0.15643952786922455,0.039307963103055954,0.1171315647661686,True,math500
trace_math500_155.jsonl,267,267,19,0.03231343254446983,0.024598296731710434,0.007715135812759399,True,math500
trace_math500_155.jsonl,337,337,220,0.34896522760391235,0.09559294581413269,0.25337228178977966,False,math500
trace_math500_155.jsonl,439,439,220,0.1330777406692505,0.0931963324546814,0.03988140821456909,False,math500
trace_math500_155.jsonl,461,461,17,0.06765367090702057,0.03862304240465164,0.029030628502368927,False,math500
trace_math500_155.jsonl,704,704,1584,0.4028942883014679,0.36006009578704834,0.042834192514419556,True,math500
trace_math500_156.jsonl,128,128,5865,0.11888885498046875,0.11530710011720657,0.0035817548632621765,False,math500
trace_math500_156.jsonl,144,144,1887,0.13739776611328125,0.030913494527339935,0.10648427158594131,True,math500
trace_math500_156.jsonl,202,202,426,0.035966336727142334,0.02222270891070366,0.013743627816438675,False,math500
trace_math500_156.jsonl,824,824,220,0.13473016023635864,0.06621529906988144,0.0685148611664772,False,math500
trace_math500_156.jsonl,831,831,220,0.3982681632041931,0.12084081023931503,0.2774273529648781,False,math500
trace_math500_157.jsonl,14,14,220,0.4590582251548767,0.08636103570461273,0.372697189450264,False,math500
trace_math500_157.jsonl,113,113,220,0.04028812795877457,0.015605119988322258,0.02468300797045231,False,math500
trace_math500_157.jsonl,126,126,11,0.036557428538799286,0.013400007970631123,0.023157420568168163,True,math500
trace_math500_157.jsonl,175,175,11,0.12079917639493942,0.049787066876888275,0.07101210951805115,False,math500
trace_math500_157.jsonl,282,282,220,0.2579090893268585,0.1353352814912796,0.12257380783557892,False,math500
trace_math500_157.jsonl,309,309,220,0.6761176586151123,0.4221879541873932,0.2539297044277191,False,math500
trace_math500_157.jsonl,311,311,220,0.08484955132007599,0.08081239461898804,0.004037156701087952,False,math500
trace_math500_157.jsonl,478,478,220,0.2808629274368286,0.08256737887859344,0.19829554855823517,True,math500
trace_math500_159.jsonl,304,304,220,0.6121168732643127,0.2862251400947571,0.32589173316955566,False,math500
trace_math500_159.jsonl,310,310,220,0.12617246806621552,0.10685011744499207,0.01932235062122345,True,math500
trace_math500_159.jsonl,413,413,220,0.7008157968521118,0.4505152702331543,0.2503005266189575,False,math500
trace_math500_159.jsonl,594,594,220,0.5537598133087158,0.08997683227062225,0.46378298103809357,False,math500
trace_math500_159.jsonl,641,641,220,0.16372962296009064,0.11666630208492279,0.04706332087516785,False,math500
trace_math500_160.jsonl,96,96,220,0.4555911421775818,0.07430259883403778,0.381288543343544,False,math500
trace_math500_160.jsonl,197,197,220,0.21007148921489716,0.15607449412345886,0.05399699509143829,False,math500
trace_math500_160.jsonl,225,225,220,0.4795750677585602,0.2336101531982422,0.245964914560318,True,math500
trace_math500_160.jsonl,275,275,220,0.24577318131923676,0.08962604403495789,0.15614713728427887,False,math500
trace_math500_161.jsonl,15,15,311,0.09542637318372726,0.0724397599697113,0.02298661321401596,False,math500
trace_math500_161.jsonl,51,51,220,0.2705163061618805,0.15729859471321106,0.11321771144866943,True,math500
trace_math500_161.jsonl,235,235,220,0.14588533341884613,0.10768816620111465,0.038197167217731476,True,math500
trace_math500_161.jsonl,460,460,30490,0.2976183295249939,0.12540937960147858,0.17220894992351532,False,math500
trace_math500_162.jsonl,217,217,527,0.14501260221004486,0.10519356280565262,0.03981903940439224,False,math500
trace_math500_162.jsonl,471,471,374,0.7167224287986755,0.3859110176563263,0.33081141114234924,True,math500
trace_math500_162.jsonl,730,730,374,0.3214058578014374,0.2845529615879059,0.036852896213531494,False,math500
trace_math500_164.jsonl,3,3,420,0.06199653074145317,0.055758874863386154,0.006237655878067017,False,math500
trace_math500_164.jsonl,124,124,40521,0.08106672763824463,0.029555529356002808,0.05151119828224182,True,math500
trace_math500_164.jsonl,515,515,8,0.031570713967084885,0.00899633951485157,0.022574374452233315,False,math500
trace_math500_166.jsonl,190,190,11,0.7895717024803162,0.48522406816482544,0.3043476343154907,True,math500
trace_math500_166.jsonl,314,314,220,0.1675458699464798,0.050571098923683167,0.11697477102279663,False,math500
trace_math500_166.jsonl,348,348,11,0.3192361295223236,0.09374400973320007,0.22549211978912354,False,math500
trace_math500_167.jsonl,201,201,220,0.7309306859970093,0.545818567276001,0.1851121187210083,False,math500
trace_math500_168.jsonl,443,443,499,0.5599162578582764,0.4240473806858063,0.1358688771724701,False,math500
trace_math500_170.jsonl,431,431,220,0.2648109495639801,0.17158177495002747,0.09322917461395264,False,math500
trace_math500_170.jsonl,769,769,279,0.12454387545585632,0.1175813302397728,0.006962545216083527,True,math500
trace_math500_171.jsonl,60,60,11,0.06786606460809708,0.02261679619550705,0.04524926841259003,False,math500
trace_math500_173.jsonl,18,18,279,0.13672614097595215,0.1261463612318039,0.010579779744148254,False,math500
trace_math500_173.jsonl,673,673,220,0.363646924495697,0.17651048302650452,0.1871364414691925,False,math500
trace_math500_174.jsonl,140,140,11,0.06636970490217209,0.057304564863443375,0.009065140038728714,True,math500
trace_math500_174.jsonl,157,157,279,0.24182522296905518,0.22976388037204742,0.012061342597007751,False,math500
trace_math500_175.jsonl,250,250,220,0.5107263922691345,0.3572580814361572,0.1534683108329773,True,math500
trace_math500_175.jsonl,691,691,220,0.29771798849105835,0.1746245175600052,0.12309347093105316,True,math500
trace_math500_176.jsonl,476,476,220,0.05485836789011955,0.029497861862182617,0.025360506027936935,False,math500
trace_math500_176.jsonl,821,821,311,0.2864786982536316,0.21395443379878998,0.07252426445484161,False,math500
trace_math500_176.jsonl,862,862,311,0.09167657047510147,0.07863260805606842,0.01304396241903305,False,math500
trace_math500_177.jsonl,45,45,11,0.15908080339431763,0.04834962263703346,0.11073118075728416,False,math500
trace_math500_177.jsonl,478,478,279,0.4050860106945038,0.26497364044189453,0.14011237025260925,False,math500
trace_math500_177.jsonl,691,691,220,0.012369638308882713,0.011372438631951809,0.0009971996769309044,True,math500
trace_math500_177.jsonl,767,767,220,0.15456072986125946,0.09785985946655273,0.056700870394706726,True,math500
trace_math500_178.jsonl,6,6,220,0.27288752794265747,0.19160032272338867,0.0812872052192688,False,math500
trace_math500_178.jsonl,37,37,220,0.4888874888420105,0.4627780318260193,0.02610945701599121,False,math500
trace_math500_178.jsonl,38,38,220,0.7082071304321289,0.3817876875400543,0.3264194428920746,False,math500
trace_math500_178.jsonl,51,51,220,0.6140447854995728,0.5269629955291748,0.08708178997039795,True,math500
trace_math500_178.jsonl,451,451,596,0.23059046268463135,0.18679669499397278,0.04379376769065857,False,math500
trace_math500_179.jsonl,254,254,220,0.5592107772827148,0.5426297187805176,0.016581058502197266,False,math500
trace_math500_179.jsonl,354,354,220,0.7474369406700134,0.16793477535247803,0.5795021653175354,False,math500
trace_math500_179.jsonl,540,540,220,0.42446306347846985,0.1593082845211029,0.26515477895736694,False,math500
trace_math500_179.jsonl,642,642,220,0.1331760436296463,0.02474284917116165,0.10843319445848465,True,math500
trace_math500_179.jsonl,711,711,279,0.4043847620487213,0.07062362134456635,0.33376114070415497,False,math500
trace_math500_180.jsonl,199,199,11,0.18372797966003418,0.1271357238292694,0.05659225583076477,True,math500
trace_math500_180.jsonl,659,659,1403,0.6694186925888062,0.2636829614639282,0.40573573112487793,True,math500
trace_math500_180.jsonl,711,711,311,0.7238411903381348,0.17946529388427734,0.5443758964538574,True,math500
trace_math500_180.jsonl,873,873,1403,0.5605438351631165,0.46663543581962585,0.0939083993434906,False,math500
trace_math500_181.jsonl,469,469,13,0.03855447098612785,0.007755329366773367,0.030799141619354486,False,math500
trace_math500_181.jsonl,550,550,8765,0.14387568831443787,0.014832456596195698,0.12904323171824217,True,math500
trace_math500_181.jsonl,652,652,311,0.13568226993083954,0.021329669281840324,0.11435260064899921,False,math500
trace_math500_181.jsonl,751,751,13,0.06998084485530853,0.022972960025072098,0.047007884830236435,False,math500
trace_math500_182.jsonl,1,1,11,0.028744077309966087,0.01882336661219597,0.009920710697770119,True,math500
trace_math500_182.jsonl,38,38,24524,0.09459235519170761,0.02503451146185398,0.06955784372985363,False,math500
trace_math500_183.jsonl,422,422,220,0.13029491901397705,0.03408471867442131,0.09621020033955574,False,math500
trace_math500_185.jsonl,146,146,6037,0.2918427586555481,0.06430353969335556,0.22753921896219254,False,math500
trace_math500_188.jsonl,252,252,220,0.1563691794872284,0.12788285315036774,0.028486326336860657,False,math500
trace_math500_188.jsonl,368,368,220,0.3944814205169678,0.24055545032024384,0.15392597019672394,False,math500
trace_math500_190.jsonl,129,129,382,0.18284116685390472,0.08568895608186722,0.0971522107720375,False,math500
trace_math500_190.jsonl,192,192,220,0.1129579022526741,0.06076257303357124,0.05219532921910286,False,math500
trace_math500_190.jsonl,261,261,220,0.16972284018993378,0.04713745042681694,0.12258538976311684,False,math500
trace_math500_190.jsonl,317,317,220,0.13926613330841064,0.03907831758260727,0.10018781572580338,False,math500
trace_math500_190.jsonl,515,515,220,0.1836872696876526,0.07272327691316605,0.11096399277448654,False,math500
trace_math500_191.jsonl,83,83,220,0.16333620250225067,0.060644011944532394,0.10269219055771828,False,math500
trace_math500_192.jsonl,107,107,279,0.32557618618011475,0.16581624746322632,0.15975993871688843,True,math500
trace_math500_192.jsonl,448,448,279,0.6987811326980591,0.32465246319770813,0.37412866950035095,False,math500
trace_math500_192.jsonl,877,877,11,0.33612221479415894,0.1621333807706833,0.17398883402347565,True,math500
trace_math500_193.jsonl,188,188,11781,0.09675731509923935,0.019688228145241737,0.07706908695399761,False,math500
trace_math500_193.jsonl,248,248,3488,0.390628844499588,0.05027565360069275,0.34035319089889526,False,math500
trace_math500_194.jsonl,688,688,279,0.21905410289764404,0.046316102147102356,0.1727380007505417,False,math500
trace_math500_195.jsonl,385,385,320,0.11261383444070816,0.05299805849790573,0.05961577594280243,False,math500
trace_math500_195.jsonl,697,697,279,0.10602356493473053,0.06939303874969482,0.036630526185035706,False,math500
trace_math500_196.jsonl,1,1,11,0.046736858785152435,0.03862304240465164,0.008113816380500793,True,math500
trace_math500_197.jsonl,719,719,220,0.309404194355011,0.26214244961738586,0.04726174473762512,False,math500
trace_math500_199.jsonl,21,21,3152,0.19103239476680756,0.18498140573501587,0.006050989031791687,True,math500
trace_math500_199.jsonl,225,225,220,0.7753341197967529,0.748051643371582,0.0272824764251709,True,math500
trace_math500_199.jsonl,434,434,220,0.4878608286380768,0.4505152702331543,0.037345558404922485,False,math500
trace_math500_199.jsonl,458,458,220,0.5369013547897339,0.036639049649238586,0.5002623051404953,True,math500