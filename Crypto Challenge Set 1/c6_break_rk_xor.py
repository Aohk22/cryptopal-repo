from pprint import pprint
import base64
import itertools

KEYSIZE = range(2, 41)

def hamming_distance(s1: bytes, s2: bytes):
    assert len(s1) == len(s2)
    total_count = 0
    per_byte_count = 0
    for b1, b2 in zip(s1,s2): # byte level
        xored_val = b1 ^ b2

        while xored_val != 0: # bit level
            if xored_val & 1 == 1:
                per_byte_count += 1
            xored_val = xored_val >> 1
        
        total_count += per_byte_count
        per_byte_count = 0
    return total_count


# def levenshtein_distance(s1, s2):
#     if len(s1) < len(s2):
#         return levenshtein_distance(s2, s1)
#     if len(s2) == 0:
#         return len(s1)
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[j + 1] + 1
#             deletions = current_row[j] + 1
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#     return previous_row[-1]


def to_blocks(raw_data: bytes, block_size: int) -> list:
    return [raw_data[i*block_size:(i+1)*block_size] for i in range(0, len(raw_data)-5)]


def get_hamming_distances(raw_data: bytes) -> list:
    hds = list()
    for ks in KEYSIZE:
        hd_list = list()
        blocks = to_blocks(raw_data, ks)
        block_pairs = itertools.combinations(blocks, 2)
        for pair in block_pairs:
            if len(pair[0]) != len(pair[1]):
                print(pair[0], pair[1]); exit()
            hd_list.append(hamming_distance(pair[0], pair[1]))
        hd_avg_ks = sum(hd_list)/len(hd_list)
        hd_normalized = hd_avg_ks/ks
        hds.append({'keysize': ks, 'hd_normalized': hd_normalized})
    sorted_hds = sorted(hds, key=lambda x: x['hd_normalized'])
    return sorted_hds[:50]


if __name__ == '__main__':
    hdt1 = b'this is a test'
    hdt2 = b'wokka wokka!!!'
    hd_test = hamming_distance(hdt1, hdt2)
    print(f'Test hamming distance {hd_test}')
    ct_b64 = open('6.txt', 'r').read().strip()
    ct_raw = base64.b64decode(ct_b64)

    hds = get_hamming_distances(ct_raw)
    pprint(hds)