from pprint import pprint
from c3_one_byte_xcipher import brute_force_xor, char_stats

lines = [bytes.fromhex(line) for line in open('4.txt').readlines()]
base_text = open('arwav.txt', 'rb').read().lower()
base_stats = char_stats(base_text)

line_scores = list()
for i, byte_str in enumerate(lines):
    result = brute_force_xor(byte_str, base_stats, top=1)[0]
    result['index'] = i
    line_scores.append(result)

line_scores_sorted = sorted(line_scores, key=lambda x: x['Score'])
pprint(line_scores_sorted[:3])

# Find string that is single-byte XOR'ed
# Sample output
# [{'Score': 0.02747, 'Text': b'Now that the party is jumping\n', 'index': 170},
#  {'Score': 0.03289,
#   'Text': b'tzmEdLo7c5eXo;Xh\x8c\x8dlbfnem\x9e\x10iDW_',
#   'index': 215},
#  {'Score': 0.03592,
#   'Text': b'\x109sf\xd1\xcenz(\xd6adb6\xd1ixcj\x1fm\xc1\x1fz8>?rt-',
#   'index': 192}]