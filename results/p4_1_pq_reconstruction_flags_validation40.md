# P4.1 pq Reconstruction Flags

Tolerance: 1e-06
Total rows processed: 26767
Invalid rows: 110
Invalid %: 0.410954%

Root cause note: unresolved (execution-path numerical drift vs context/state reconstruction mismatch).
Policy note: flagged rows are excluded from confirmatory P4.1 statistics and are not corrected/substituted.

## Breakdown by Dataset
- livecodebench: rows=24609, invalid=98, invalid_pct=0.398228%
- math500: rows=2158, invalid=12, invalid_pct=0.556070%

## Breakdown by Row Type
- post_rejection: rows=8704, invalid=44, invalid_pct=0.505515%
- normal: rows=18063, invalid=66, invalid_pct=0.365388%

## Breakdown by Position
- position=0: rows=40, invalid=0, invalid_pct=0.000000%
- position=1: rows=40, invalid=2, invalid_pct=5.000000%
- position=2: rows=40, invalid=1, invalid_pct=2.500000%
- position=3: rows=40, invalid=0, invalid_pct=0.000000%
- position=4: rows=40, invalid=0, invalid_pct=0.000000%
- position=5: rows=40, invalid=1, invalid_pct=2.500000%
- position=6: rows=40, invalid=0, invalid_pct=0.000000%
- position=7: rows=40, invalid=0, invalid_pct=0.000000%
- position=8: rows=40, invalid=0, invalid_pct=0.000000%
- position=9: rows=40, invalid=1, invalid_pct=2.500000%
- position=10: rows=40, invalid=1, invalid_pct=2.500000%
- position=11: rows=40, invalid=0, invalid_pct=0.000000%
- position=12: rows=40, invalid=1, invalid_pct=2.500000%
- position=13: rows=40, invalid=0, invalid_pct=0.000000%
- position=14: rows=40, invalid=0, invalid_pct=0.000000%
- position=15: rows=40, invalid=0, invalid_pct=0.000000%
- position=16: rows=40, invalid=1, invalid_pct=2.500000%
- position=17: rows=40, invalid=1, invalid_pct=2.500000%
- position=18: rows=40, invalid=0, invalid_pct=0.000000%
- position=19: rows=40, invalid=0, invalid_pct=0.000000%
- position=20: rows=40, invalid=0, invalid_pct=0.000000%
- position=21: rows=40, invalid=0, invalid_pct=0.000000%
- position=22: rows=40, invalid=0, invalid_pct=0.000000%
- position=23: rows=40, invalid=0, invalid_pct=0.000000%
- position=24: rows=40, invalid=0, invalid_pct=0.000000%
- position=25: rows=40, invalid=0, invalid_pct=0.000000%
- position=26: rows=40, invalid=0, invalid_pct=0.000000%
- position=27: rows=40, invalid=0, invalid_pct=0.000000%
- position=28: rows=40, invalid=0, invalid_pct=0.000000%
- position=29: rows=40, invalid=1, invalid_pct=2.500000%
- position=30: rows=40, invalid=0, invalid_pct=0.000000%
- position=31: rows=40, invalid=1, invalid_pct=2.500000%
- position=32: rows=40, invalid=1, invalid_pct=2.500000%
- position=33: rows=40, invalid=0, invalid_pct=0.000000%
- position=34: rows=40, invalid=0, invalid_pct=0.000000%
- position=35: rows=40, invalid=0, invalid_pct=0.000000%
- position=36: rows=40, invalid=0, invalid_pct=0.000000%
- position=37: rows=40, invalid=0, invalid_pct=0.000000%
- position=38: rows=40, invalid=0, invalid_pct=0.000000%
- position=39: rows=40, invalid=0, invalid_pct=0.000000%
- position=40: rows=40, invalid=0, invalid_pct=0.000000%
- position=41: rows=40, invalid=0, invalid_pct=0.000000%
- position=42: rows=40, invalid=0, invalid_pct=0.000000%
- position=43: rows=40, invalid=0, invalid_pct=0.000000%
- position=44: rows=40, invalid=0, invalid_pct=0.000000%
- position=45: rows=40, invalid=0, invalid_pct=0.000000%
- position=46: rows=40, invalid=1, invalid_pct=2.500000%
- position=47: rows=40, invalid=0, invalid_pct=0.000000%
- position=48: rows=40, invalid=0, invalid_pct=0.000000%
- position=49: rows=40, invalid=0, invalid_pct=0.000000%
- position=50: rows=40, invalid=0, invalid_pct=0.000000%
- position=51: rows=40, invalid=1, invalid_pct=2.500000%
- position=52: rows=40, invalid=0, invalid_pct=0.000000%
- position=53: rows=40, invalid=0, invalid_pct=0.000000%
- position=54: rows=40, invalid=1, invalid_pct=2.500000%
- position=55: rows=40, invalid=0, invalid_pct=0.000000%
- position=56: rows=40, invalid=0, invalid_pct=0.000000%
- position=57: rows=40, invalid=0, invalid_pct=0.000000%
- position=58: rows=40, invalid=0, invalid_pct=0.000000%
- position=59: rows=40, invalid=1, invalid_pct=2.500000%
- position=60: rows=40, invalid=1, invalid_pct=2.500000%
- position=61: rows=40, invalid=0, invalid_pct=0.000000%
- position=62: rows=40, invalid=0, invalid_pct=0.000000%
- position=63: rows=40, invalid=0, invalid_pct=0.000000%
- position=64: rows=40, invalid=0, invalid_pct=0.000000%
- position=65: rows=40, invalid=0, invalid_pct=0.000000%
- position=66: rows=40, invalid=0, invalid_pct=0.000000%
- position=67: rows=40, invalid=0, invalid_pct=0.000000%
- position=68: rows=40, invalid=0, invalid_pct=0.000000%
- position=69: rows=40, invalid=0, invalid_pct=0.000000%
- position=70: rows=40, invalid=0, invalid_pct=0.000000%
- position=71: rows=40, invalid=0, invalid_pct=0.000000%
- position=72: rows=40, invalid=0, invalid_pct=0.000000%
- position=73: rows=40, invalid=1, invalid_pct=2.500000%
- position=74: rows=40, invalid=0, invalid_pct=0.000000%
- position=75: rows=40, invalid=0, invalid_pct=0.000000%
- position=76: rows=40, invalid=0, invalid_pct=0.000000%
- position=77: rows=40, invalid=0, invalid_pct=0.000000%
- position=78: rows=40, invalid=0, invalid_pct=0.000000%
- position=79: rows=40, invalid=0, invalid_pct=0.000000%
- position=80: rows=40, invalid=0, invalid_pct=0.000000%
- position=81: rows=40, invalid=0, invalid_pct=0.000000%
- position=82: rows=40, invalid=0, invalid_pct=0.000000%
- position=83: rows=40, invalid=1, invalid_pct=2.500000%
- position=84: rows=40, invalid=0, invalid_pct=0.000000%
- position=85: rows=40, invalid=0, invalid_pct=0.000000%
- position=86: rows=40, invalid=0, invalid_pct=0.000000%
- position=87: rows=40, invalid=1, invalid_pct=2.500000%
- position=88: rows=40, invalid=0, invalid_pct=0.000000%
- position=89: rows=40, invalid=0, invalid_pct=0.000000%
- position=90: rows=40, invalid=0, invalid_pct=0.000000%
- position=91: rows=40, invalid=0, invalid_pct=0.000000%
- position=92: rows=40, invalid=0, invalid_pct=0.000000%
- position=93: rows=40, invalid=0, invalid_pct=0.000000%
- position=94: rows=40, invalid=0, invalid_pct=0.000000%
- position=95: rows=40, invalid=0, invalid_pct=0.000000%
- position=96: rows=40, invalid=0, invalid_pct=0.000000%
- position=97: rows=40, invalid=0, invalid_pct=0.000000%
- position=98: rows=40, invalid=0, invalid_pct=0.000000%
- position=99: rows=40, invalid=1, invalid_pct=2.500000%
- position=100: rows=40, invalid=0, invalid_pct=0.000000%
- position=101: rows=40, invalid=0, invalid_pct=0.000000%
- position=102: rows=40, invalid=0, invalid_pct=0.000000%
- position=103: rows=40, invalid=0, invalid_pct=0.000000%
- position=104: rows=40, invalid=0, invalid_pct=0.000000%
- position=105: rows=40, invalid=1, invalid_pct=2.500000%
- position=106: rows=40, invalid=0, invalid_pct=0.000000%
- position=107: rows=40, invalid=0, invalid_pct=0.000000%
- position=108: rows=40, invalid=0, invalid_pct=0.000000%
- position=109: rows=40, invalid=0, invalid_pct=0.000000%
- position=110: rows=40, invalid=0, invalid_pct=0.000000%
- position=111: rows=40, invalid=0, invalid_pct=0.000000%
- position=112: rows=40, invalid=0, invalid_pct=0.000000%
- position=113: rows=40, invalid=0, invalid_pct=0.000000%
- position=114: rows=40, invalid=0, invalid_pct=0.000000%
- position=115: rows=40, invalid=0, invalid_pct=0.000000%
- position=116: rows=40, invalid=0, invalid_pct=0.000000%
- position=117: rows=40, invalid=0, invalid_pct=0.000000%
- position=118: rows=40, invalid=0, invalid_pct=0.000000%
- position=119: rows=40, invalid=0, invalid_pct=0.000000%
- position=120: rows=40, invalid=1, invalid_pct=2.500000%
- position=121: rows=40, invalid=0, invalid_pct=0.000000%
- position=122: rows=40, invalid=1, invalid_pct=2.500000%
- position=123: rows=40, invalid=1, invalid_pct=2.500000%
- position=124: rows=40, invalid=0, invalid_pct=0.000000%
- position=125: rows=40, invalid=0, invalid_pct=0.000000%
- position=126: rows=40, invalid=0, invalid_pct=0.000000%
- position=127: rows=40, invalid=0, invalid_pct=0.000000%
- position=128: rows=40, invalid=0, invalid_pct=0.000000%
- position=129: rows=40, invalid=0, invalid_pct=0.000000%
- position=130: rows=40, invalid=0, invalid_pct=0.000000%
- position=131: rows=40, invalid=0, invalid_pct=0.000000%
- position=132: rows=40, invalid=0, invalid_pct=0.000000%
- position=133: rows=40, invalid=0, invalid_pct=0.000000%
- position=134: rows=40, invalid=0, invalid_pct=0.000000%
- position=135: rows=40, invalid=0, invalid_pct=0.000000%
- position=136: rows=40, invalid=0, invalid_pct=0.000000%
- position=137: rows=40, invalid=0, invalid_pct=0.000000%
- position=138: rows=40, invalid=0, invalid_pct=0.000000%
- position=139: rows=40, invalid=0, invalid_pct=0.000000%
- position=140: rows=40, invalid=1, invalid_pct=2.500000%
- position=141: rows=40, invalid=0, invalid_pct=0.000000%
- position=142: rows=40, invalid=0, invalid_pct=0.000000%
- position=143: rows=40, invalid=0, invalid_pct=0.000000%
- position=144: rows=40, invalid=0, invalid_pct=0.000000%
- position=145: rows=40, invalid=0, invalid_pct=0.000000%
- position=146: rows=40, invalid=0, invalid_pct=0.000000%
- position=147: rows=40, invalid=0, invalid_pct=0.000000%
- position=148: rows=40, invalid=0, invalid_pct=0.000000%
- position=149: rows=40, invalid=0, invalid_pct=0.000000%
- position=150: rows=40, invalid=0, invalid_pct=0.000000%
- position=151: rows=40, invalid=0, invalid_pct=0.000000%
- position=152: rows=40, invalid=0, invalid_pct=0.000000%
- position=153: rows=40, invalid=0, invalid_pct=0.000000%
- position=154: rows=40, invalid=0, invalid_pct=0.000000%
- position=155: rows=40, invalid=0, invalid_pct=0.000000%
- position=156: rows=40, invalid=0, invalid_pct=0.000000%
- position=157: rows=40, invalid=0, invalid_pct=0.000000%
- position=158: rows=40, invalid=0, invalid_pct=0.000000%
- position=159: rows=40, invalid=0, invalid_pct=0.000000%
- position=160: rows=40, invalid=0, invalid_pct=0.000000%
- position=161: rows=40, invalid=0, invalid_pct=0.000000%
- position=162: rows=40, invalid=0, invalid_pct=0.000000%
- position=163: rows=40, invalid=1, invalid_pct=2.500000%
- position=164: rows=40, invalid=0, invalid_pct=0.000000%
- position=165: rows=40, invalid=0, invalid_pct=0.000000%
- position=166: rows=40, invalid=0, invalid_pct=0.000000%
- position=167: rows=40, invalid=0, invalid_pct=0.000000%
- position=168: rows=40, invalid=0, invalid_pct=0.000000%
- position=169: rows=40, invalid=0, invalid_pct=0.000000%
- position=170: rows=40, invalid=0, invalid_pct=0.000000%
- position=171: rows=40, invalid=0, invalid_pct=0.000000%
- position=172: rows=40, invalid=0, invalid_pct=0.000000%
- position=173: rows=40, invalid=0, invalid_pct=0.000000%
- position=174: rows=40, invalid=1, invalid_pct=2.500000%
- position=175: rows=40, invalid=0, invalid_pct=0.000000%
- position=176: rows=40, invalid=0, invalid_pct=0.000000%
- position=177: rows=40, invalid=0, invalid_pct=0.000000%
- position=178: rows=40, invalid=0, invalid_pct=0.000000%
- position=179: rows=40, invalid=0, invalid_pct=0.000000%
- position=180: rows=40, invalid=0, invalid_pct=0.000000%
- position=181: rows=40, invalid=0, invalid_pct=0.000000%
- position=182: rows=40, invalid=0, invalid_pct=0.000000%
- position=183: rows=40, invalid=0, invalid_pct=0.000000%
- position=184: rows=40, invalid=0, invalid_pct=0.000000%
- position=185: rows=40, invalid=0, invalid_pct=0.000000%
- position=186: rows=40, invalid=0, invalid_pct=0.000000%
- position=187: rows=40, invalid=0, invalid_pct=0.000000%
- position=188: rows=40, invalid=0, invalid_pct=0.000000%
- position=189: rows=40, invalid=1, invalid_pct=2.500000%
- position=190: rows=40, invalid=1, invalid_pct=2.500000%
- position=191: rows=40, invalid=0, invalid_pct=0.000000%
- position=192: rows=40, invalid=0, invalid_pct=0.000000%
- position=193: rows=40, invalid=0, invalid_pct=0.000000%
- position=194: rows=40, invalid=0, invalid_pct=0.000000%
- position=195: rows=40, invalid=0, invalid_pct=0.000000%
- position=196: rows=40, invalid=0, invalid_pct=0.000000%
- position=197: rows=40, invalid=0, invalid_pct=0.000000%
- position=198: rows=40, invalid=0, invalid_pct=0.000000%
- position=199: rows=40, invalid=1, invalid_pct=2.500000%
- position=200: rows=40, invalid=0, invalid_pct=0.000000%
- position=201: rows=40, invalid=0, invalid_pct=0.000000%
- position=202: rows=40, invalid=0, invalid_pct=0.000000%
- position=203: rows=40, invalid=0, invalid_pct=0.000000%
- position=204: rows=40, invalid=0, invalid_pct=0.000000%
- position=205: rows=40, invalid=0, invalid_pct=0.000000%
- position=206: rows=40, invalid=1, invalid_pct=2.500000%
- position=207: rows=40, invalid=1, invalid_pct=2.500000%
- position=208: rows=40, invalid=1, invalid_pct=2.500000%
- position=209: rows=40, invalid=0, invalid_pct=0.000000%
- position=210: rows=40, invalid=0, invalid_pct=0.000000%
- position=211: rows=40, invalid=3, invalid_pct=7.500000%
- position=212: rows=40, invalid=0, invalid_pct=0.000000%
- position=213: rows=40, invalid=0, invalid_pct=0.000000%
- position=214: rows=40, invalid=0, invalid_pct=0.000000%
- position=215: rows=40, invalid=0, invalid_pct=0.000000%
- position=216: rows=40, invalid=1, invalid_pct=2.500000%
- position=217: rows=40, invalid=1, invalid_pct=2.500000%
- position=218: rows=40, invalid=0, invalid_pct=0.000000%
- position=219: rows=40, invalid=0, invalid_pct=0.000000%
- position=220: rows=40, invalid=0, invalid_pct=0.000000%
- position=221: rows=40, invalid=0, invalid_pct=0.000000%
- position=222: rows=40, invalid=0, invalid_pct=0.000000%
- position=223: rows=40, invalid=0, invalid_pct=0.000000%
- position=224: rows=40, invalid=0, invalid_pct=0.000000%
- position=225: rows=40, invalid=0, invalid_pct=0.000000%
- position=226: rows=40, invalid=0, invalid_pct=0.000000%
- position=227: rows=40, invalid=0, invalid_pct=0.000000%
- position=228: rows=40, invalid=0, invalid_pct=0.000000%
- position=229: rows=40, invalid=0, invalid_pct=0.000000%
- position=230: rows=40, invalid=0, invalid_pct=0.000000%
- position=231: rows=40, invalid=0, invalid_pct=0.000000%
- position=232: rows=40, invalid=0, invalid_pct=0.000000%
- position=233: rows=40, invalid=0, invalid_pct=0.000000%
- position=234: rows=40, invalid=0, invalid_pct=0.000000%
- position=235: rows=40, invalid=0, invalid_pct=0.000000%
- position=236: rows=40, invalid=0, invalid_pct=0.000000%
- position=237: rows=40, invalid=0, invalid_pct=0.000000%
- position=238: rows=40, invalid=0, invalid_pct=0.000000%
- position=239: rows=40, invalid=1, invalid_pct=2.500000%
- position=240: rows=40, invalid=0, invalid_pct=0.000000%
- position=241: rows=40, invalid=0, invalid_pct=0.000000%
- position=242: rows=40, invalid=0, invalid_pct=0.000000%
- position=243: rows=40, invalid=0, invalid_pct=0.000000%
- position=244: rows=40, invalid=0, invalid_pct=0.000000%
- position=245: rows=40, invalid=0, invalid_pct=0.000000%
- position=246: rows=40, invalid=0, invalid_pct=0.000000%
- position=247: rows=40, invalid=1, invalid_pct=2.500000%
- position=248: rows=40, invalid=1, invalid_pct=2.500000%
- position=249: rows=40, invalid=1, invalid_pct=2.500000%
- position=250: rows=40, invalid=1, invalid_pct=2.500000%
- position=251: rows=40, invalid=0, invalid_pct=0.000000%
- position=252: rows=40, invalid=0, invalid_pct=0.000000%
- position=253: rows=40, invalid=0, invalid_pct=0.000000%
- position=254: rows=40, invalid=0, invalid_pct=0.000000%
- position=255: rows=40, invalid=0, invalid_pct=0.000000%
- position=256: rows=40, invalid=0, invalid_pct=0.000000%
- position=257: rows=40, invalid=0, invalid_pct=0.000000%
- position=258: rows=40, invalid=0, invalid_pct=0.000000%
- position=259: rows=40, invalid=0, invalid_pct=0.000000%
- position=260: rows=40, invalid=0, invalid_pct=0.000000%
- position=261: rows=40, invalid=0, invalid_pct=0.000000%
- position=262: rows=40, invalid=0, invalid_pct=0.000000%
- position=263: rows=40, invalid=1, invalid_pct=2.500000%
- position=264: rows=40, invalid=0, invalid_pct=0.000000%
- position=265: rows=40, invalid=0, invalid_pct=0.000000%
- position=266: rows=40, invalid=0, invalid_pct=0.000000%
- position=267: rows=40, invalid=0, invalid_pct=0.000000%
- position=268: rows=40, invalid=0, invalid_pct=0.000000%
- position=269: rows=40, invalid=0, invalid_pct=0.000000%
- position=270: rows=40, invalid=1, invalid_pct=2.500000%
- position=271: rows=40, invalid=1, invalid_pct=2.500000%
- position=272: rows=40, invalid=0, invalid_pct=0.000000%
- position=273: rows=40, invalid=0, invalid_pct=0.000000%
- position=274: rows=40, invalid=0, invalid_pct=0.000000%
- position=275: rows=40, invalid=0, invalid_pct=0.000000%
- position=276: rows=40, invalid=0, invalid_pct=0.000000%
- position=277: rows=40, invalid=0, invalid_pct=0.000000%
- position=278: rows=40, invalid=0, invalid_pct=0.000000%
- position=279: rows=40, invalid=1, invalid_pct=2.500000%
- position=280: rows=40, invalid=0, invalid_pct=0.000000%
- position=281: rows=40, invalid=0, invalid_pct=0.000000%
- position=282: rows=40, invalid=0, invalid_pct=0.000000%
- position=283: rows=40, invalid=0, invalid_pct=0.000000%
- position=284: rows=40, invalid=0, invalid_pct=0.000000%
- position=285: rows=40, invalid=0, invalid_pct=0.000000%
- position=286: rows=40, invalid=0, invalid_pct=0.000000%
- position=287: rows=40, invalid=0, invalid_pct=0.000000%
- position=288: rows=40, invalid=0, invalid_pct=0.000000%
- position=289: rows=40, invalid=0, invalid_pct=0.000000%
- position=290: rows=40, invalid=0, invalid_pct=0.000000%
- position=291: rows=40, invalid=0, invalid_pct=0.000000%
- position=292: rows=40, invalid=0, invalid_pct=0.000000%
- position=293: rows=40, invalid=0, invalid_pct=0.000000%
- position=294: rows=40, invalid=0, invalid_pct=0.000000%
- position=295: rows=40, invalid=0, invalid_pct=0.000000%
- position=296: rows=40, invalid=0, invalid_pct=0.000000%
- position=297: rows=40, invalid=0, invalid_pct=0.000000%
- position=298: rows=40, invalid=0, invalid_pct=0.000000%
- position=299: rows=40, invalid=0, invalid_pct=0.000000%
- position=300: rows=40, invalid=0, invalid_pct=0.000000%
- position=301: rows=40, invalid=0, invalid_pct=0.000000%
- position=302: rows=40, invalid=0, invalid_pct=0.000000%
- position=303: rows=40, invalid=0, invalid_pct=0.000000%
- position=304: rows=40, invalid=0, invalid_pct=0.000000%
- position=305: rows=40, invalid=0, invalid_pct=0.000000%
- position=306: rows=40, invalid=0, invalid_pct=0.000000%
- position=307: rows=40, invalid=0, invalid_pct=0.000000%
- position=308: rows=40, invalid=0, invalid_pct=0.000000%
- position=309: rows=40, invalid=0, invalid_pct=0.000000%
- position=310: rows=40, invalid=0, invalid_pct=0.000000%
- position=311: rows=40, invalid=0, invalid_pct=0.000000%
- position=312: rows=40, invalid=0, invalid_pct=0.000000%
- position=313: rows=40, invalid=1, invalid_pct=2.500000%
- position=314: rows=40, invalid=0, invalid_pct=0.000000%
- position=315: rows=40, invalid=1, invalid_pct=2.500000%
- position=316: rows=40, invalid=1, invalid_pct=2.500000%
- position=317: rows=40, invalid=0, invalid_pct=0.000000%
- position=318: rows=40, invalid=0, invalid_pct=0.000000%
- position=319: rows=40, invalid=0, invalid_pct=0.000000%
- position=320: rows=40, invalid=1, invalid_pct=2.500000%
- position=321: rows=40, invalid=0, invalid_pct=0.000000%
- position=322: rows=40, invalid=0, invalid_pct=0.000000%
- position=323: rows=40, invalid=0, invalid_pct=0.000000%
- position=324: rows=40, invalid=0, invalid_pct=0.000000%
- position=325: rows=40, invalid=0, invalid_pct=0.000000%
- position=326: rows=40, invalid=0, invalid_pct=0.000000%
- position=327: rows=40, invalid=0, invalid_pct=0.000000%
- position=328: rows=40, invalid=0, invalid_pct=0.000000%
- position=329: rows=40, invalid=0, invalid_pct=0.000000%
- position=330: rows=40, invalid=1, invalid_pct=2.500000%
- position=331: rows=40, invalid=1, invalid_pct=2.500000%
- position=332: rows=40, invalid=0, invalid_pct=0.000000%
- position=333: rows=40, invalid=0, invalid_pct=0.000000%
- position=334: rows=40, invalid=0, invalid_pct=0.000000%
- position=335: rows=40, invalid=0, invalid_pct=0.000000%
- position=336: rows=40, invalid=0, invalid_pct=0.000000%
- position=337: rows=40, invalid=0, invalid_pct=0.000000%
- position=338: rows=40, invalid=0, invalid_pct=0.000000%
- position=339: rows=40, invalid=0, invalid_pct=0.000000%
- position=340: rows=40, invalid=1, invalid_pct=2.500000%
- position=341: rows=40, invalid=0, invalid_pct=0.000000%
- position=342: rows=40, invalid=0, invalid_pct=0.000000%
- position=343: rows=40, invalid=0, invalid_pct=0.000000%
- position=344: rows=40, invalid=1, invalid_pct=2.500000%
- position=345: rows=40, invalid=0, invalid_pct=0.000000%
- position=346: rows=40, invalid=0, invalid_pct=0.000000%
- position=347: rows=40, invalid=0, invalid_pct=0.000000%
- position=348: rows=40, invalid=0, invalid_pct=0.000000%
- position=349: rows=40, invalid=0, invalid_pct=0.000000%
- position=350: rows=40, invalid=0, invalid_pct=0.000000%
- position=351: rows=40, invalid=1, invalid_pct=2.500000%
- position=352: rows=40, invalid=0, invalid_pct=0.000000%
- position=353: rows=40, invalid=0, invalid_pct=0.000000%
- position=354: rows=40, invalid=0, invalid_pct=0.000000%
- position=355: rows=40, invalid=0, invalid_pct=0.000000%
- position=356: rows=40, invalid=0, invalid_pct=0.000000%
- position=357: rows=40, invalid=0, invalid_pct=0.000000%
- position=358: rows=40, invalid=0, invalid_pct=0.000000%
- position=359: rows=40, invalid=0, invalid_pct=0.000000%
- position=360: rows=40, invalid=0, invalid_pct=0.000000%
- position=361: rows=40, invalid=1, invalid_pct=2.500000%
- position=362: rows=40, invalid=0, invalid_pct=0.000000%
- position=363: rows=40, invalid=0, invalid_pct=0.000000%
- position=364: rows=40, invalid=0, invalid_pct=0.000000%
- position=365: rows=40, invalid=0, invalid_pct=0.000000%
- position=366: rows=40, invalid=0, invalid_pct=0.000000%
- position=367: rows=40, invalid=0, invalid_pct=0.000000%
- position=368: rows=40, invalid=0, invalid_pct=0.000000%
- position=369: rows=40, invalid=0, invalid_pct=0.000000%
- position=370: rows=40, invalid=0, invalid_pct=0.000000%
- position=371: rows=40, invalid=0, invalid_pct=0.000000%
- position=372: rows=40, invalid=0, invalid_pct=0.000000%
- position=373: rows=40, invalid=0, invalid_pct=0.000000%
- position=374: rows=40, invalid=1, invalid_pct=2.500000%
- position=375: rows=40, invalid=0, invalid_pct=0.000000%
- position=376: rows=40, invalid=0, invalid_pct=0.000000%
- position=377: rows=40, invalid=0, invalid_pct=0.000000%
- position=378: rows=40, invalid=0, invalid_pct=0.000000%
- position=379: rows=40, invalid=1, invalid_pct=2.500000%
- position=380: rows=40, invalid=0, invalid_pct=0.000000%
- position=381: rows=40, invalid=0, invalid_pct=0.000000%
- position=382: rows=40, invalid=0, invalid_pct=0.000000%
- position=383: rows=40, invalid=0, invalid_pct=0.000000%
- position=384: rows=40, invalid=0, invalid_pct=0.000000%
- position=385: rows=40, invalid=0, invalid_pct=0.000000%
- position=386: rows=40, invalid=0, invalid_pct=0.000000%
- position=387: rows=40, invalid=0, invalid_pct=0.000000%
- position=388: rows=40, invalid=0, invalid_pct=0.000000%
- position=389: rows=40, invalid=0, invalid_pct=0.000000%
- position=390: rows=40, invalid=0, invalid_pct=0.000000%
- position=391: rows=40, invalid=0, invalid_pct=0.000000%
- position=392: rows=40, invalid=0, invalid_pct=0.000000%
- position=393: rows=40, invalid=0, invalid_pct=0.000000%
- position=394: rows=40, invalid=0, invalid_pct=0.000000%
- position=395: rows=40, invalid=0, invalid_pct=0.000000%
- position=396: rows=40, invalid=0, invalid_pct=0.000000%
- position=397: rows=40, invalid=0, invalid_pct=0.000000%
- position=398: rows=40, invalid=0, invalid_pct=0.000000%
- position=399: rows=40, invalid=0, invalid_pct=0.000000%
- position=400: rows=40, invalid=1, invalid_pct=2.500000%
- position=401: rows=40, invalid=0, invalid_pct=0.000000%
- position=402: rows=40, invalid=0, invalid_pct=0.000000%
- position=403: rows=40, invalid=0, invalid_pct=0.000000%
- position=404: rows=40, invalid=1, invalid_pct=2.500000%
- position=405: rows=40, invalid=1, invalid_pct=2.500000%
- position=406: rows=40, invalid=0, invalid_pct=0.000000%
- position=407: rows=40, invalid=0, invalid_pct=0.000000%
- position=408: rows=40, invalid=0, invalid_pct=0.000000%
- position=409: rows=40, invalid=0, invalid_pct=0.000000%
- position=410: rows=40, invalid=0, invalid_pct=0.000000%
- position=411: rows=40, invalid=0, invalid_pct=0.000000%
- position=412: rows=40, invalid=1, invalid_pct=2.500000%
- position=413: rows=40, invalid=0, invalid_pct=0.000000%
- position=414: rows=40, invalid=0, invalid_pct=0.000000%
- position=415: rows=40, invalid=0, invalid_pct=0.000000%
- position=416: rows=40, invalid=0, invalid_pct=0.000000%
- position=417: rows=40, invalid=0, invalid_pct=0.000000%
- position=418: rows=40, invalid=1, invalid_pct=2.500000%
- position=419: rows=40, invalid=0, invalid_pct=0.000000%
- position=420: rows=40, invalid=0, invalid_pct=0.000000%
- position=421: rows=40, invalid=0, invalid_pct=0.000000%
- position=422: rows=40, invalid=0, invalid_pct=0.000000%
- position=423: rows=40, invalid=0, invalid_pct=0.000000%
- position=424: rows=40, invalid=0, invalid_pct=0.000000%
- position=425: rows=40, invalid=0, invalid_pct=0.000000%
- position=426: rows=40, invalid=0, invalid_pct=0.000000%
- position=427: rows=40, invalid=0, invalid_pct=0.000000%
- position=428: rows=40, invalid=0, invalid_pct=0.000000%
- position=429: rows=40, invalid=0, invalid_pct=0.000000%
- position=430: rows=40, invalid=0, invalid_pct=0.000000%
- position=431: rows=40, invalid=0, invalid_pct=0.000000%
- position=432: rows=40, invalid=0, invalid_pct=0.000000%
- position=433: rows=40, invalid=1, invalid_pct=2.500000%
- position=434: rows=40, invalid=0, invalid_pct=0.000000%
- position=435: rows=40, invalid=1, invalid_pct=2.500000%
- position=436: rows=40, invalid=1, invalid_pct=2.500000%
- position=437: rows=40, invalid=0, invalid_pct=0.000000%
- position=438: rows=40, invalid=0, invalid_pct=0.000000%
- position=439: rows=39, invalid=0, invalid_pct=0.000000%
- position=440: rows=39, invalid=0, invalid_pct=0.000000%
- position=441: rows=39, invalid=0, invalid_pct=0.000000%
- position=442: rows=39, invalid=1, invalid_pct=2.564103%
- position=443: rows=39, invalid=0, invalid_pct=0.000000%
- position=444: rows=39, invalid=0, invalid_pct=0.000000%
- position=445: rows=39, invalid=0, invalid_pct=0.000000%
- position=446: rows=39, invalid=0, invalid_pct=0.000000%
- position=447: rows=39, invalid=0, invalid_pct=0.000000%
- position=448: rows=39, invalid=0, invalid_pct=0.000000%
- position=449: rows=39, invalid=0, invalid_pct=0.000000%
- position=450: rows=39, invalid=1, invalid_pct=2.564103%
- position=451: rows=39, invalid=0, invalid_pct=0.000000%
- position=452: rows=39, invalid=0, invalid_pct=0.000000%
- position=453: rows=39, invalid=0, invalid_pct=0.000000%
- position=454: rows=39, invalid=1, invalid_pct=2.564103%
- position=455: rows=39, invalid=1, invalid_pct=2.564103%
- position=456: rows=39, invalid=0, invalid_pct=0.000000%
- position=457: rows=39, invalid=0, invalid_pct=0.000000%
- position=458: rows=39, invalid=0, invalid_pct=0.000000%
- position=459: rows=39, invalid=0, invalid_pct=0.000000%
- position=460: rows=39, invalid=0, invalid_pct=0.000000%
- position=461: rows=39, invalid=0, invalid_pct=0.000000%
- position=462: rows=39, invalid=0, invalid_pct=0.000000%
- position=463: rows=39, invalid=0, invalid_pct=0.000000%
- position=464: rows=39, invalid=0, invalid_pct=0.000000%
- position=465: rows=39, invalid=0, invalid_pct=0.000000%
- position=466: rows=39, invalid=0, invalid_pct=0.000000%
- position=467: rows=39, invalid=0, invalid_pct=0.000000%
- position=468: rows=39, invalid=1, invalid_pct=2.564103%
- position=469: rows=39, invalid=2, invalid_pct=5.128205%
- position=470: rows=39, invalid=0, invalid_pct=0.000000%
- position=471: rows=39, invalid=1, invalid_pct=2.564103%
- position=472: rows=39, invalid=1, invalid_pct=2.564103%
- position=473: rows=39, invalid=1, invalid_pct=2.564103%
- position=474: rows=39, invalid=0, invalid_pct=0.000000%
- position=475: rows=39, invalid=0, invalid_pct=0.000000%
- position=476: rows=39, invalid=0, invalid_pct=0.000000%
- position=477: rows=39, invalid=0, invalid_pct=0.000000%
- position=478: rows=39, invalid=0, invalid_pct=0.000000%
- position=479: rows=39, invalid=0, invalid_pct=0.000000%
- position=480: rows=39, invalid=0, invalid_pct=0.000000%
- position=481: rows=39, invalid=0, invalid_pct=0.000000%
- position=482: rows=39, invalid=0, invalid_pct=0.000000%
- position=483: rows=39, invalid=1, invalid_pct=2.564103%
- position=484: rows=39, invalid=0, invalid_pct=0.000000%
- position=485: rows=39, invalid=0, invalid_pct=0.000000%
- position=486: rows=39, invalid=0, invalid_pct=0.000000%
- position=487: rows=39, invalid=0, invalid_pct=0.000000%
- position=488: rows=39, invalid=0, invalid_pct=0.000000%
- position=489: rows=39, invalid=1, invalid_pct=2.564103%
- position=490: rows=39, invalid=1, invalid_pct=2.564103%
- position=491: rows=39, invalid=0, invalid_pct=0.000000%
- position=492: rows=39, invalid=0, invalid_pct=0.000000%
- position=493: rows=39, invalid=0, invalid_pct=0.000000%
- position=494: rows=39, invalid=0, invalid_pct=0.000000%
- position=495: rows=39, invalid=0, invalid_pct=0.000000%
- position=496: rows=39, invalid=0, invalid_pct=0.000000%
- position=497: rows=39, invalid=0, invalid_pct=0.000000%
- position=498: rows=39, invalid=0, invalid_pct=0.000000%
- position=499: rows=39, invalid=0, invalid_pct=0.000000%
- position=500: rows=39, invalid=0, invalid_pct=0.000000%
- position=501: rows=39, invalid=0, invalid_pct=0.000000%
- position=502: rows=39, invalid=0, invalid_pct=0.000000%
- position=503: rows=39, invalid=0, invalid_pct=0.000000%
- position=504: rows=39, invalid=0, invalid_pct=0.000000%
- position=505: rows=39, invalid=0, invalid_pct=0.000000%
- position=506: rows=39, invalid=0, invalid_pct=0.000000%
- position=507: rows=39, invalid=0, invalid_pct=0.000000%
- position=508: rows=39, invalid=0, invalid_pct=0.000000%
- position=509: rows=39, invalid=0, invalid_pct=0.000000%
- position=510: rows=39, invalid=0, invalid_pct=0.000000%
- position=511: rows=39, invalid=0, invalid_pct=0.000000%
- position=512: rows=39, invalid=1, invalid_pct=2.564103%
- position=513: rows=39, invalid=0, invalid_pct=0.000000%
- position=514: rows=39, invalid=0, invalid_pct=0.000000%
- position=515: rows=39, invalid=1, invalid_pct=2.564103%
- position=516: rows=39, invalid=0, invalid_pct=0.000000%
- position=517: rows=39, invalid=0, invalid_pct=0.000000%
- position=518: rows=39, invalid=0, invalid_pct=0.000000%
- position=519: rows=39, invalid=1, invalid_pct=2.564103%
- position=520: rows=39, invalid=0, invalid_pct=0.000000%
- position=521: rows=39, invalid=0, invalid_pct=0.000000%
- position=522: rows=39, invalid=0, invalid_pct=0.000000%
- position=523: rows=39, invalid=1, invalid_pct=2.564103%
- position=524: rows=39, invalid=0, invalid_pct=0.000000%
- position=525: rows=39, invalid=0, invalid_pct=0.000000%
- position=526: rows=39, invalid=0, invalid_pct=0.000000%
- position=527: rows=39, invalid=1, invalid_pct=2.564103%
- position=528: rows=39, invalid=0, invalid_pct=0.000000%
- position=529: rows=39, invalid=0, invalid_pct=0.000000%
- position=530: rows=39, invalid=0, invalid_pct=0.000000%
- position=531: rows=39, invalid=1, invalid_pct=2.564103%
- position=532: rows=39, invalid=0, invalid_pct=0.000000%
- position=533: rows=39, invalid=0, invalid_pct=0.000000%
- position=534: rows=39, invalid=0, invalid_pct=0.000000%
- position=535: rows=38, invalid=0, invalid_pct=0.000000%
- position=536: rows=38, invalid=0, invalid_pct=0.000000%
- position=537: rows=38, invalid=0, invalid_pct=0.000000%
- position=538: rows=38, invalid=0, invalid_pct=0.000000%
- position=539: rows=38, invalid=0, invalid_pct=0.000000%
- position=540: rows=38, invalid=0, invalid_pct=0.000000%
- position=541: rows=37, invalid=0, invalid_pct=0.000000%
- position=542: rows=37, invalid=0, invalid_pct=0.000000%
- position=543: rows=36, invalid=1, invalid_pct=2.777778%
- position=544: rows=36, invalid=1, invalid_pct=2.777778%
- position=545: rows=36, invalid=0, invalid_pct=0.000000%
- position=546: rows=36, invalid=0, invalid_pct=0.000000%
- position=547: rows=36, invalid=0, invalid_pct=0.000000%
- position=548: rows=36, invalid=0, invalid_pct=0.000000%
- position=549: rows=36, invalid=0, invalid_pct=0.000000%
- position=550: rows=36, invalid=1, invalid_pct=2.777778%
- position=551: rows=36, invalid=1, invalid_pct=2.777778%
- position=552: rows=36, invalid=0, invalid_pct=0.000000%
- position=553: rows=36, invalid=0, invalid_pct=0.000000%
- position=554: rows=36, invalid=0, invalid_pct=0.000000%
- position=555: rows=36, invalid=0, invalid_pct=0.000000%
- position=556: rows=36, invalid=0, invalid_pct=0.000000%
- position=557: rows=36, invalid=0, invalid_pct=0.000000%
- position=558: rows=36, invalid=0, invalid_pct=0.000000%
- position=559: rows=36, invalid=1, invalid_pct=2.777778%
- position=560: rows=36, invalid=0, invalid_pct=0.000000%
- position=561: rows=36, invalid=0, invalid_pct=0.000000%
- position=562: rows=36, invalid=0, invalid_pct=0.000000%
- position=563: rows=36, invalid=0, invalid_pct=0.000000%
- position=564: rows=36, invalid=0, invalid_pct=0.000000%
- position=565: rows=36, invalid=0, invalid_pct=0.000000%
- position=566: rows=36, invalid=0, invalid_pct=0.000000%
- position=567: rows=36, invalid=1, invalid_pct=2.777778%
- position=568: rows=36, invalid=0, invalid_pct=0.000000%
- position=569: rows=36, invalid=0, invalid_pct=0.000000%
- position=570: rows=36, invalid=0, invalid_pct=0.000000%
- position=571: rows=36, invalid=0, invalid_pct=0.000000%
- position=572: rows=36, invalid=0, invalid_pct=0.000000%
- position=573: rows=36, invalid=0, invalid_pct=0.000000%
- position=574: rows=36, invalid=1, invalid_pct=2.777778%
- position=575: rows=36, invalid=0, invalid_pct=0.000000%
- position=576: rows=36, invalid=0, invalid_pct=0.000000%
- position=577: rows=35, invalid=1, invalid_pct=2.857143%
- position=578: rows=34, invalid=0, invalid_pct=0.000000%
- position=579: rows=34, invalid=1, invalid_pct=2.941176%
- position=580: rows=34, invalid=0, invalid_pct=0.000000%
- position=581: rows=34, invalid=0, invalid_pct=0.000000%
- position=582: rows=34, invalid=0, invalid_pct=0.000000%
- position=583: rows=34, invalid=0, invalid_pct=0.000000%
- position=584: rows=34, invalid=0, invalid_pct=0.000000%
- position=585: rows=34, invalid=0, invalid_pct=0.000000%
- position=586: rows=34, invalid=0, invalid_pct=0.000000%
- position=587: rows=34, invalid=0, invalid_pct=0.000000%
- position=588: rows=34, invalid=0, invalid_pct=0.000000%
- position=589: rows=34, invalid=0, invalid_pct=0.000000%
- position=590: rows=34, invalid=0, invalid_pct=0.000000%
- position=591: rows=34, invalid=0, invalid_pct=0.000000%
- position=592: rows=33, invalid=0, invalid_pct=0.000000%
- position=593: rows=33, invalid=0, invalid_pct=0.000000%
- position=594: rows=33, invalid=0, invalid_pct=0.000000%
- position=595: rows=33, invalid=0, invalid_pct=0.000000%
- position=596: rows=31, invalid=0, invalid_pct=0.000000%
- position=597: rows=31, invalid=1, invalid_pct=3.225806%
- position=598: rows=31, invalid=0, invalid_pct=0.000000%
- position=599: rows=31, invalid=0, invalid_pct=0.000000%
- position=600: rows=31, invalid=0, invalid_pct=0.000000%
- position=601: rows=31, invalid=0, invalid_pct=0.000000%
- position=602: rows=31, invalid=0, invalid_pct=0.000000%
- position=603: rows=31, invalid=0, invalid_pct=0.000000%
- position=604: rows=31, invalid=0, invalid_pct=0.000000%
- position=605: rows=31, invalid=0, invalid_pct=0.000000%
- position=606: rows=31, invalid=0, invalid_pct=0.000000%
- position=607: rows=31, invalid=0, invalid_pct=0.000000%
- position=608: rows=31, invalid=0, invalid_pct=0.000000%
- position=609: rows=31, invalid=0, invalid_pct=0.000000%
- position=610: rows=31, invalid=0, invalid_pct=0.000000%
- position=611: rows=31, invalid=0, invalid_pct=0.000000%
- position=612: rows=31, invalid=0, invalid_pct=0.000000%
- position=613: rows=31, invalid=0, invalid_pct=0.000000%
- position=614: rows=30, invalid=0, invalid_pct=0.000000%
- position=615: rows=29, invalid=0, invalid_pct=0.000000%
- position=616: rows=28, invalid=0, invalid_pct=0.000000%
- position=617: rows=28, invalid=0, invalid_pct=0.000000%
- position=618: rows=28, invalid=0, invalid_pct=0.000000%
- position=619: rows=28, invalid=0, invalid_pct=0.000000%
- position=620: rows=28, invalid=0, invalid_pct=0.000000%
- position=621: rows=28, invalid=1, invalid_pct=3.571429%
- position=622: rows=28, invalid=0, invalid_pct=0.000000%
- position=623: rows=28, invalid=2, invalid_pct=7.142857%
- position=624: rows=28, invalid=0, invalid_pct=0.000000%
- position=625: rows=28, invalid=1, invalid_pct=3.571429%
- position=626: rows=28, invalid=1, invalid_pct=3.571429%
- position=627: rows=28, invalid=0, invalid_pct=0.000000%
- position=628: rows=28, invalid=0, invalid_pct=0.000000%
- position=629: rows=28, invalid=0, invalid_pct=0.000000%
- position=630: rows=28, invalid=0, invalid_pct=0.000000%
- position=631: rows=28, invalid=0, invalid_pct=0.000000%
- position=632: rows=28, invalid=1, invalid_pct=3.571429%
- position=633: rows=28, invalid=0, invalid_pct=0.000000%
- position=634: rows=28, invalid=1, invalid_pct=3.571429%
- position=635: rows=28, invalid=0, invalid_pct=0.000000%
- position=636: rows=28, invalid=0, invalid_pct=0.000000%
- position=637: rows=28, invalid=0, invalid_pct=0.000000%
- position=638: rows=28, invalid=0, invalid_pct=0.000000%
- position=639: rows=27, invalid=0, invalid_pct=0.000000%
- position=640: rows=27, invalid=0, invalid_pct=0.000000%
- position=641: rows=27, invalid=0, invalid_pct=0.000000%
- position=642: rows=27, invalid=0, invalid_pct=0.000000%
- position=643: rows=27, invalid=0, invalid_pct=0.000000%
- position=644: rows=26, invalid=0, invalid_pct=0.000000%
- position=645: rows=26, invalid=0, invalid_pct=0.000000%
- position=646: rows=26, invalid=0, invalid_pct=0.000000%
- position=647: rows=26, invalid=0, invalid_pct=0.000000%
- position=648: rows=26, invalid=1, invalid_pct=3.846154%
- position=649: rows=26, invalid=1, invalid_pct=3.846154%
- position=650: rows=26, invalid=0, invalid_pct=0.000000%
- position=651: rows=26, invalid=0, invalid_pct=0.000000%
- position=652: rows=25, invalid=1, invalid_pct=4.000000%
- position=653: rows=25, invalid=0, invalid_pct=0.000000%
- position=654: rows=25, invalid=0, invalid_pct=0.000000%
- position=655: rows=25, invalid=0, invalid_pct=0.000000%
- position=656: rows=25, invalid=0, invalid_pct=0.000000%
- position=657: rows=25, invalid=0, invalid_pct=0.000000%
- position=658: rows=25, invalid=0, invalid_pct=0.000000%
- position=659: rows=25, invalid=0, invalid_pct=0.000000%
- position=660: rows=25, invalid=0, invalid_pct=0.000000%
- position=661: rows=25, invalid=0, invalid_pct=0.000000%
- position=662: rows=25, invalid=0, invalid_pct=0.000000%
- position=663: rows=23, invalid=0, invalid_pct=0.000000%
- position=664: rows=23, invalid=0, invalid_pct=0.000000%
- position=665: rows=23, invalid=0, invalid_pct=0.000000%
- position=666: rows=23, invalid=0, invalid_pct=0.000000%
- position=667: rows=23, invalid=0, invalid_pct=0.000000%
- position=668: rows=22, invalid=0, invalid_pct=0.000000%
- position=669: rows=21, invalid=0, invalid_pct=0.000000%
- position=670: rows=21, invalid=0, invalid_pct=0.000000%
- position=671: rows=20, invalid=0, invalid_pct=0.000000%
- position=672: rows=20, invalid=0, invalid_pct=0.000000%
- position=673: rows=20, invalid=0, invalid_pct=0.000000%
- position=674: rows=20, invalid=0, invalid_pct=0.000000%
- position=675: rows=20, invalid=0, invalid_pct=0.000000%
- position=676: rows=20, invalid=0, invalid_pct=0.000000%
- position=677: rows=19, invalid=0, invalid_pct=0.000000%
- position=678: rows=19, invalid=0, invalid_pct=0.000000%
- position=679: rows=19, invalid=0, invalid_pct=0.000000%
- position=680: rows=19, invalid=0, invalid_pct=0.000000%
- position=681: rows=19, invalid=0, invalid_pct=0.000000%
- position=682: rows=19, invalid=0, invalid_pct=0.000000%
- position=683: rows=19, invalid=0, invalid_pct=0.000000%
- position=684: rows=18, invalid=0, invalid_pct=0.000000%
- position=685: rows=17, invalid=0, invalid_pct=0.000000%
- position=686: rows=17, invalid=0, invalid_pct=0.000000%
- position=687: rows=15, invalid=0, invalid_pct=0.000000%
- position=688: rows=15, invalid=0, invalid_pct=0.000000%
- position=689: rows=15, invalid=0, invalid_pct=0.000000%
- position=690: rows=15, invalid=0, invalid_pct=0.000000%
- position=691: rows=15, invalid=0, invalid_pct=0.000000%
- position=692: rows=15, invalid=0, invalid_pct=0.000000%
- position=693: rows=15, invalid=0, invalid_pct=0.000000%
- position=694: rows=15, invalid=0, invalid_pct=0.000000%
- position=695: rows=15, invalid=0, invalid_pct=0.000000%
- position=696: rows=15, invalid=1, invalid_pct=6.666667%
- position=697: rows=14, invalid=0, invalid_pct=0.000000%
- position=698: rows=14, invalid=0, invalid_pct=0.000000%
- position=699: rows=14, invalid=0, invalid_pct=0.000000%
- position=700: rows=14, invalid=0, invalid_pct=0.000000%
- position=701: rows=14, invalid=0, invalid_pct=0.000000%
- position=702: rows=14, invalid=0, invalid_pct=0.000000%
- position=703: rows=14, invalid=0, invalid_pct=0.000000%
- position=704: rows=14, invalid=0, invalid_pct=0.000000%
- position=705: rows=14, invalid=0, invalid_pct=0.000000%
- position=706: rows=14, invalid=0, invalid_pct=0.000000%
- position=707: rows=14, invalid=0, invalid_pct=0.000000%
- position=708: rows=14, invalid=0, invalid_pct=0.000000%
- position=709: rows=13, invalid=0, invalid_pct=0.000000%
- position=710: rows=13, invalid=0, invalid_pct=0.000000%
- position=711: rows=13, invalid=0, invalid_pct=0.000000%
- position=712: rows=13, invalid=0, invalid_pct=0.000000%
- position=713: rows=13, invalid=0, invalid_pct=0.000000%
- position=714: rows=13, invalid=0, invalid_pct=0.000000%
- position=715: rows=13, invalid=0, invalid_pct=0.000000%
- position=716: rows=13, invalid=0, invalid_pct=0.000000%
- position=717: rows=13, invalid=0, invalid_pct=0.000000%
- position=718: rows=13, invalid=0, invalid_pct=0.000000%
- position=719: rows=13, invalid=0, invalid_pct=0.000000%
- position=720: rows=13, invalid=0, invalid_pct=0.000000%
- position=721: rows=12, invalid=0, invalid_pct=0.000000%
- position=722: rows=12, invalid=0, invalid_pct=0.000000%
- position=723: rows=12, invalid=0, invalid_pct=0.000000%
- position=724: rows=12, invalid=0, invalid_pct=0.000000%
- position=725: rows=12, invalid=0, invalid_pct=0.000000%
- position=726: rows=12, invalid=0, invalid_pct=0.000000%
- position=727: rows=12, invalid=0, invalid_pct=0.000000%
- position=728: rows=11, invalid=0, invalid_pct=0.000000%
- position=729: rows=11, invalid=0, invalid_pct=0.000000%
- position=730: rows=11, invalid=0, invalid_pct=0.000000%
- position=731: rows=11, invalid=0, invalid_pct=0.000000%
- position=732: rows=10, invalid=0, invalid_pct=0.000000%
- position=733: rows=10, invalid=0, invalid_pct=0.000000%
- position=734: rows=10, invalid=0, invalid_pct=0.000000%
- position=735: rows=10, invalid=0, invalid_pct=0.000000%
- position=736: rows=9, invalid=0, invalid_pct=0.000000%
- position=737: rows=8, invalid=0, invalid_pct=0.000000%
- position=738: rows=7, invalid=1, invalid_pct=14.285714%
- position=739: rows=7, invalid=0, invalid_pct=0.000000%
- position=740: rows=7, invalid=0, invalid_pct=0.000000%
- position=741: rows=7, invalid=0, invalid_pct=0.000000%
- position=742: rows=7, invalid=0, invalid_pct=0.000000%
- position=743: rows=7, invalid=0, invalid_pct=0.000000%
- position=744: rows=7, invalid=0, invalid_pct=0.000000%
- position=745: rows=7, invalid=0, invalid_pct=0.000000%
- position=746: rows=7, invalid=0, invalid_pct=0.000000%
- position=747: rows=7, invalid=0, invalid_pct=0.000000%
- position=748: rows=7, invalid=0, invalid_pct=0.000000%
- position=749: rows=7, invalid=0, invalid_pct=0.000000%
- position=750: rows=7, invalid=0, invalid_pct=0.000000%
- position=751: rows=6, invalid=1, invalid_pct=16.666667%
- position=752: rows=6, invalid=0, invalid_pct=0.000000%
- position=753: rows=6, invalid=0, invalid_pct=0.000000%
- position=754: rows=6, invalid=0, invalid_pct=0.000000%
- position=755: rows=5, invalid=0, invalid_pct=0.000000%
- position=756: rows=5, invalid=0, invalid_pct=0.000000%
- position=757: rows=5, invalid=0, invalid_pct=0.000000%
- position=758: rows=5, invalid=0, invalid_pct=0.000000%
- position=759: rows=5, invalid=0, invalid_pct=0.000000%
- position=760: rows=5, invalid=0, invalid_pct=0.000000%
- position=761: rows=5, invalid=0, invalid_pct=0.000000%
- position=762: rows=4, invalid=0, invalid_pct=0.000000%
- position=763: rows=4, invalid=0, invalid_pct=0.000000%
- position=764: rows=4, invalid=0, invalid_pct=0.000000%
- position=765: rows=4, invalid=0, invalid_pct=0.000000%
- position=766: rows=4, invalid=0, invalid_pct=0.000000%
- position=767: rows=3, invalid=0, invalid_pct=0.000000%
- position=768: rows=3, invalid=0, invalid_pct=0.000000%
- position=769: rows=3, invalid=0, invalid_pct=0.000000%
- position=770: rows=3, invalid=0, invalid_pct=0.000000%
- position=771: rows=3, invalid=0, invalid_pct=0.000000%
- position=772: rows=3, invalid=0, invalid_pct=0.000000%
- position=773: rows=3, invalid=0, invalid_pct=0.000000%
- position=774: rows=3, invalid=0, invalid_pct=0.000000%
- position=775: rows=3, invalid=0, invalid_pct=0.000000%
- position=776: rows=3, invalid=0, invalid_pct=0.000000%
- position=777: rows=3, invalid=0, invalid_pct=0.000000%
- position=778: rows=3, invalid=0, invalid_pct=0.000000%
- position=779: rows=3, invalid=0, invalid_pct=0.000000%
- position=780: rows=2, invalid=0, invalid_pct=0.000000%
- position=781: rows=2, invalid=0, invalid_pct=0.000000%
- position=782: rows=2, invalid=0, invalid_pct=0.000000%
- position=783: rows=2, invalid=0, invalid_pct=0.000000%
- position=784: rows=2, invalid=0, invalid_pct=0.000000%
- position=785: rows=2, invalid=0, invalid_pct=0.000000%
- position=786: rows=2, invalid=0, invalid_pct=0.000000%
- position=787: rows=2, invalid=0, invalid_pct=0.000000%
- position=788: rows=2, invalid=0, invalid_pct=0.000000%
- position=789: rows=2, invalid=0, invalid_pct=0.000000%
- position=790: rows=2, invalid=0, invalid_pct=0.000000%
- position=791: rows=2, invalid=0, invalid_pct=0.000000%
- position=792: rows=2, invalid=0, invalid_pct=0.000000%
- position=793: rows=2, invalid=0, invalid_pct=0.000000%
- position=794: rows=2, invalid=0, invalid_pct=0.000000%
- position=795: rows=2, invalid=0, invalid_pct=0.000000%
- position=796: rows=2, invalid=0, invalid_pct=0.000000%
- position=797: rows=2, invalid=0, invalid_pct=0.000000%
- position=798: rows=2, invalid=0, invalid_pct=0.000000%
- position=799: rows=2, invalid=0, invalid_pct=0.000000%
- position=800: rows=2, invalid=0, invalid_pct=0.000000%
- position=801: rows=2, invalid=0, invalid_pct=0.000000%
- position=802: rows=1, invalid=0, invalid_pct=0.000000%
- position=803: rows=1, invalid=0, invalid_pct=0.000000%
- position=804: rows=1, invalid=0, invalid_pct=0.000000%
- position=805: rows=1, invalid=0, invalid_pct=0.000000%
- position=806: rows=1, invalid=0, invalid_pct=0.000000%
- position=807: rows=1, invalid=0, invalid_pct=0.000000%
- position=808: rows=1, invalid=0, invalid_pct=0.000000%
- position=809: rows=1, invalid=0, invalid_pct=0.000000%
- position=810: rows=1, invalid=0, invalid_pct=0.000000%
- position=811: rows=1, invalid=0, invalid_pct=0.000000%
- position=812: rows=1, invalid=0, invalid_pct=0.000000%
- position=813: rows=1, invalid=0, invalid_pct=0.000000%
- position=814: rows=1, invalid=0, invalid_pct=0.000000%
- position=815: rows=1, invalid=0, invalid_pct=0.000000%
- position=816: rows=1, invalid=0, invalid_pct=0.000000%
- position=817: rows=1, invalid=0, invalid_pct=0.000000%
- position=818: rows=1, invalid=0, invalid_pct=0.000000%
- position=819: rows=1, invalid=0, invalid_pct=0.000000%
- position=820: rows=1, invalid=0, invalid_pct=0.000000%

## Full List of Flagged Rows
trace_id,step,position,token_id,q,draft_top1_prob,violation_magnitude,post_rejection_row,dataset
trace_livecodebench_10.jsonl,122,122,11,0.3789963126182556,0.052585624158382416,0.3264106884598732,True,livecodebench
trace_livecodebench_10.jsonl,247,247,1855,0.07343164086341858,0.061119645833969116,0.012311995029449463,False,livecodebench
trace_livecodebench_100.jsonl,46,46,13,0.1553487777709961,0.06269139051437378,0.09265738725662231,False,livecodebench
trace_livecodebench_100.jsonl,207,207,220,0.7887539267539978,0.547954797744751,0.24079912900924683,False,livecodebench
trace_livecodebench_100.jsonl,471,471,220,0.09258455038070679,0.03336023539304733,0.059224314987659454,False,livecodebench
trace_livecodebench_100.jsonl,519,519,11,0.023508351296186447,0.017891358584165573,0.005616992712020874,True,livecodebench
trace_livecodebench_100.jsonl,632,632,364,0.07627274841070175,0.06405284255743027,0.012219905853271484,False,livecodebench
trace_livecodebench_105.jsonl,105,105,11,0.04313943535089493,0.025829192250967026,0.017310243099927902,False,livecodebench
trace_livecodebench_108.jsonl,87,87,3044,0.48773378133773804,0.15993180871009827,0.32780197262763977,True,livecodebench
trace_livecodebench_108.jsonl,190,190,279,0.027058061212301254,0.02412252128124237,0.0029355399310588837,False,livecodebench
trace_livecodebench_110.jsonl,31,31,279,0.09378834068775177,0.08452540636062622,0.00926293432712555,False,livecodebench
trace_livecodebench_110.jsonl,217,217,374,0.03035784140229225,0.013140829280018806,0.017217012122273445,False,livecodebench
trace_livecodebench_110.jsonl,320,320,279,0.15438243746757507,0.0846906527876854,0.06969178467988968,False,livecodebench
trace_livecodebench_112.jsonl,60,60,220,0.392193466424942,0.11575840413570404,0.276435062289238,True,livecodebench
trace_livecodebench_112.jsonl,344,344,11,0.03602639213204384,0.034486494958400726,0.0015398971736431122,False,livecodebench
trace_livecodebench_112.jsonl,361,361,220,0.4976097345352173,0.1946175992488861,0.3029921352863312,False,livecodebench
trace_livecodebench_120.jsonl,163,163,5361,0.22828078269958496,0.06660442054271698,0.16167636215686798,False,livecodebench
trace_livecodebench_120.jsonl,527,527,374,0.02080785669386387,0.017138870432972908,0.0036689862608909607,False,livecodebench
trace_livecodebench_131.jsonl,29,29,279,0.5992173552513123,0.5720128417015076,0.027204513549804688,True,livecodebench
trace_livecodebench_131.jsonl,83,83,5540,0.011164161376655102,0.009502028115093708,0.0016621332615613937,True,livecodebench
trace_livecodebench_131.jsonl,123,123,279,0.5239579677581787,0.28594574332237244,0.23801222443580627,False,livecodebench
trace_livecodebench_131.jsonl,211,211,311,0.10345238447189331,0.04217129200696945,0.06128109246492386,False,livecodebench
trace_livecodebench_131.jsonl,271,271,311,0.26831379532814026,0.025728492066264153,0.2425853032618761,False,livecodebench
trace_livecodebench_131.jsonl,454,454,311,0.12255498021841049,0.06196100637316704,0.060593973845243454,False,livecodebench
trace_livecodebench_131.jsonl,574,574,279,0.035974808037281036,0.006063496228307486,0.02991131180897355,True,livecodebench
trace_livecodebench_131.jsonl,625,625,279,0.33550161123275757,0.10519356280565262,0.23030804842710495,False,livecodebench
trace_livecodebench_131.jsonl,626,626,279,0.8019932508468628,0.13719826936721802,0.6647949814796448,True,livecodebench
trace_livecodebench_135.jsonl,472,472,304,0.6222798228263855,0.07415761798620224,0.5481222048401833,False,livecodebench
trace_livecodebench_137.jsonl,73,73,220,0.17930017411708832,0.16875676810741425,0.010543406009674072,True,livecodebench
trace_livecodebench_137.jsonl,249,249,220,0.27790752053260803,0.10498830676078796,0.17291921377182007,False,livecodebench
trace_livecodebench_137.jsonl,468,468,11,0.053948719054460526,0.04462883993983269,0.009319879114627838,False,livecodebench
trace_livecodebench_137.jsonl,512,512,311,0.28681254386901855,0.17754775285720825,0.1092647910118103,True,livecodebench
trace_livecodebench_138.jsonl,340,340,279,0.380960613489151,0.1388155221939087,0.2421450912952423,True,livecodebench
trace_livecodebench_141.jsonl,623,623,1314,0.4443492591381073,0.1281328648328781,0.3162163943052292,False,livecodebench
trace_livecodebench_142.jsonl,400,400,872,0.3423207402229309,0.25457391142845154,0.08774682879447937,True,livecodebench
trace_livecodebench_145.jsonl,189,189,279,0.09778770804405212,0.062082141637802124,0.03570556640625,False,livecodebench
trace_livecodebench_145.jsonl,433,433,343,0.271029531955719,0.24434363842010498,0.026685893535614014,True,livecodebench
trace_livecodebench_145.jsonl,515,515,279,0.32378122210502625,0.31558719277381897,0.008194029331207275,False,livecodebench
trace_livecodebench_148.jsonl,51,51,311,0.08821678161621094,0.03103448450565338,0.057182297110557556,False,livecodebench
trace_livecodebench_148.jsonl,330,330,220,0.06323765963315964,0.031461700797080994,0.031775958836078644,False,livecodebench
trace_livecodebench_148.jsonl,331,331,220,0.28558316826820374,0.14921846985816956,0.13636469841003418,False,livecodebench
trace_livecodebench_17.jsonl,263,263,1963,0.13811838626861572,0.11666630208492279,0.021452084183692932,True,livecodebench
trace_livecodebench_17.jsonl,543,543,279,0.38945266604423523,0.044891104102134705,0.3445615619421005,False,livecodebench
trace_livecodebench_18.jsonl,16,16,279,0.27125656604766846,0.10096627473831177,0.1702902913093567,False,livecodebench
trace_livecodebench_18.jsonl,469,469,11,0.04820001870393753,0.039307963103055954,0.008892055600881577,True,livecodebench
trace_livecodebench_18.jsonl,649,649,279,0.4066418707370758,0.3412310779094696,0.0654107928276062,False,livecodebench
trace_livecodebench_19.jsonl,379,379,11,0.1938074678182602,0.025132494047284126,0.16867497377097607,True,livecodebench
trace_livecodebench_19.jsonl,404,404,11,0.02223403938114643,0.02055264636874199,0.0016813930124044418,True,livecodebench
trace_livecodebench_25.jsonl,248,248,279,0.180490642786026,0.14113931357860565,0.03935132920742035,True,livecodebench
trace_livecodebench_25.jsonl,279,279,279,0.18504777550697327,0.0851883515715599,0.09985942393541336,False,livecodebench
trace_livecodebench_25.jsonl,623,623,369,0.05894666910171509,0.03885000944137573,0.020096659660339355,True,livecodebench
trace_livecodebench_29.jsonl,140,140,364,0.31200075149536133,0.12863436341285706,0.18336638808250427,True,livecodebench
trace_livecodebench_29.jsonl,316,316,364,0.032082393765449524,0.025829192250967026,0.006253201514482498,False,livecodebench
trace_livecodebench_29.jsonl,435,435,279,0.18677978217601776,0.1194329708814621,0.06734681129455566,False,livecodebench
trace_livecodebench_29.jsonl,597,597,11,0.07400639355182648,0.046770624816417694,0.027235768735408783,False,livecodebench
trace_livecodebench_31.jsonl,10,10,264,0.6679843068122864,0.17445406317710876,0.4935302436351776,False,livecodebench
trace_livecodebench_31.jsonl,54,54,279,0.5963971614837646,0.07062362134456635,0.5257735401391983,True,livecodebench
trace_livecodebench_31.jsonl,211,211,842,0.5710982084274292,0.5522524118423462,0.018845796585083008,True,livecodebench
trace_livecodebench_31.jsonl,738,738,842,0.6524924039840698,0.22976388037204742,0.4227285236120224,True,livecodebench
trace_livecodebench_42.jsonl,250,250,11,0.5280073285102844,0.302609384059906,0.22539794445037842,False,livecodebench
trace_livecodebench_42.jsonl,483,483,311,0.048083748668432236,0.04135562479496002,0.006728123873472214,True,livecodebench
trace_livecodebench_45.jsonl,544,544,220,0.5222638845443726,0.2039574682712555,0.31830641627311707,False,livecodebench
trace_livecodebench_45.jsonl,551,551,220,0.5326911807060242,0.17876562476158142,0.35392555594444275,False,livecodebench
trace_livecodebench_45.jsonl,579,579,220,0.2542423903942108,0.09634269028902054,0.15789970010519028,False,livecodebench
trace_livecodebench_45.jsonl,696,696,220,0.46954649686813354,0.4616495370864868,0.007896959781646729,False,livecodebench
trace_livecodebench_5.jsonl,199,199,220,0.7581033110618591,0.18264783918857574,0.5754554718732834,True,livecodebench
trace_livecodebench_51.jsonl,59,59,311,0.6412448287010193,0.24626006186008453,0.39498476684093475,False,livecodebench
trace_livecodebench_62.jsonl,12,12,925,0.3182210624217987,0.3131312429904938,0.005089819431304932,True,livecodebench
trace_livecodebench_62.jsonl,17,17,1855,0.2049332559108734,0.11919993162155151,0.0857333242893219,True,livecodebench
trace_livecodebench_62.jsonl,99,99,370,0.987339437007904,0.2752600312232971,0.7120794057846069,True,livecodebench
trace_livecodebench_62.jsonl,208,208,311,0.20303143560886383,0.12178856879472733,0.0812428668141365,True,livecodebench
trace_livecodebench_62.jsonl,239,239,925,0.18624204397201538,0.1677708476781845,0.01847119629383087,True,livecodebench
trace_livecodebench_62.jsonl,313,313,374,0.12667065858840942,0.0608813650906086,0.06578929349780083,True,livecodebench
trace_livecodebench_65.jsonl,211,211,220,0.2957450747489929,0.07576808333396912,0.2199769914150238,False,livecodebench
trace_livecodebench_65.jsonl,216,216,220,0.4692726731300354,0.3935224413871765,0.07575023174285889,True,livecodebench
trace_livecodebench_65.jsonl,270,270,220,0.3435026705265045,0.25833046436309814,0.08517220616340637,False,livecodebench
trace_livecodebench_65.jsonl,559,559,3160,0.27963414788246155,0.11919993162155151,0.16043421626091003,True,livecodebench
trace_livecodebench_66.jsonl,174,174,220,0.15004435181617737,0.12989671528339386,0.02014763653278351,False,livecodebench
trace_livecodebench_66.jsonl,374,374,220,0.07997375726699829,0.019881438463926315,0.060092318803071976,True,livecodebench
trace_livecodebench_68.jsonl,2,2,311,0.5347715020179749,0.47607138752937317,0.058700114488601685,False,livecodebench
trace_livecodebench_68.jsonl,5,5,311,0.09976286441087723,0.07847918570041656,0.021283678710460663,False,livecodebench
trace_livecodebench_68.jsonl,442,442,311,0.518410861492157,0.1377352476119995,0.38067561388015747,False,livecodebench
trace_livecodebench_68.jsonl,473,473,311,0.6331742405891418,0.39390695095062256,0.2392672896385193,False,livecodebench
trace_livecodebench_68.jsonl,489,489,279,0.35693421959877014,0.20099160075187683,0.1559426188468933,False,livecodebench
trace_livecodebench_68.jsonl,634,634,279,0.37740424275398254,0.37058377265930176,0.006820470094680786,False,livecodebench
trace_livecodebench_72.jsonl,32,32,11,0.7011275291442871,0.26967254281044006,0.43145498633384705,False,livecodebench
trace_livecodebench_72.jsonl,490,490,311,0.3162984251976013,0.1281328648328781,0.1881655603647232,True,livecodebench
trace_livecodebench_72.jsonl,648,648,320,0.2768193781375885,0.2013845294713974,0.0754348486661911,True,livecodebench
trace_livecodebench_73.jsonl,436,436,11,0.13540486991405487,0.044891104102134705,0.09051376581192017,True,livecodebench
trace_livecodebench_73.jsonl,531,531,11,0.07476963102817535,0.04454176127910614,0.030227869749069214,False,livecodebench
trace_livecodebench_77.jsonl,523,523,311,0.6087067723274231,0.48522406816482544,0.12348270416259766,False,livecodebench
trace_livecodebench_77.jsonl,567,567,311,0.49874478578567505,0.24244214594364166,0.2563026398420334,True,livecodebench
trace_livecodebench_8.jsonl,9,9,382,0.08627323806285858,0.05320548638701439,0.03306775167584419,False,livecodebench
trace_livecodebench_8.jsonl,120,120,320,0.281271368265152,0.0586635023355484,0.22260786592960358,False,livecodebench
trace_livecodebench_83.jsonl,405,405,220,0.23826411366462708,0.14364221692085266,0.09462189674377441,False,livecodebench
trace_livecodebench_83.jsonl,412,412,279,0.2033347636461258,0.06858458369970322,0.13475017994642258,False,livecodebench
trace_livecodebench_83.jsonl,450,450,11,0.09011721611022949,0.03208222612738609,0.0580349899828434,False,livecodebench
trace_livecodebench_83.jsonl,455,455,220,0.4680725038051605,0.16711677610874176,0.30095572769641876,False,livecodebench
trace_math500_146.jsonl,1,1,11,0.08313611149787903,0.02803732082247734,0.05509879067540169,True,math500
trace_math500_146.jsonl,206,206,220,0.09677431732416153,0.039154719561338425,0.057619597762823105,True,math500
trace_math500_146.jsonl,315,315,323,0.13133765757083893,0.06845075637102127,0.06288690119981766,True,math500
trace_math500_146.jsonl,351,351,220,0.10782254487276077,0.045776501297950745,0.06204604357481003,False,math500
trace_math500_146.jsonl,418,418,20,0.0540207177400589,0.023517746478319168,0.03050297126173973,True,math500
trace_math500_146.jsonl,577,577,220,0.19276253879070282,0.09671976417303085,0.09604277461767197,False,math500
trace_math500_146.jsonl,621,621,220,0.18640007078647614,0.1677708476781845,0.018629223108291626,False,math500
trace_math500_181.jsonl,469,469,13,0.03855447098612785,0.007755329366773367,0.030799141619354486,False,math500
trace_math500_181.jsonl,550,550,8765,0.14387568831443787,0.014832456596195698,0.12904323171824217,True,math500
trace_math500_181.jsonl,652,652,311,0.13568226993083954,0.021329669281840324,0.11435260064899921,False,math500
trace_math500_181.jsonl,751,751,13,0.06998084485530853,0.022972960025072098,0.047007884830236435,False,math500
trace_math500_196.jsonl,1,1,11,0.046736858785152435,0.03862304240465164,0.008113816380500793,True,math500