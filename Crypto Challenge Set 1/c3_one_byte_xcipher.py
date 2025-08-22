from string import ascii_lowercase

def char_stats(raw: bytes):
    base_freq = dict()
    base_percentage = dict()
    for byte in raw:
        char = chr(byte)
        if char in ascii_lowercase:
            base_freq[char] = base_freq.get(char, 1) + 1

    for char in base_freq.keys():
        percentage = base_freq.get(char)/sum(base_freq.values())
        base_percentage[char] = round(percentage, 4)
    return base_freq, base_percentage

def score(text: bytes, base_stats: tuple) -> float:
    '''Calculate total difference of character percentages then average it.'''
    _, base_percentages = base_stats
    _, text_percentages = char_stats(text)
    differences = list()
    for char, percentage in text_percentages.items():
        differences.append(abs(percentage - base_percentages.get(char)))
    try:
        avg = sum(differences)/len(differences)
    except:
        return 9999.
    return round(avg, 5)


def xor(bstr1: bytes, bstr2: bytes) -> bytes:
    '''Repeating key XOR.'''
    if len(bstr2) > len(bstr1):
        bstr1, bstr2 = bstr2, bstr1
    bstr2 = bstr2 * (len(bstr1)//len(bstr2)) + bstr2[:len(bstr1)%len(bstr2)]
    return b''.join([bytes([b1 ^ b2]) for b1, b2 in zip(bstr1, bstr2)])

def brute_force_xor(ct: bytes, base_stats: tuple, top=6):
    '''Single byte key XOR cipher. Returns text with scores.'''
    scores = list()
    for key in range(256):
        byte_key = bytes([key])
        temp_pt = xor(ct, byte_key)
        scores.append({'Score': score(temp_pt, base_stats), 'Text': temp_pt})
    scores_sorted = sorted(scores, key=lambda x: x['Score'])
    return scores_sorted[:top]

def main():
    from pprint import pprint
    the_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext_bytes = bytes.fromhex(the_string)
    base_text = open('arwav.txt', 'rb').read().lower()
    base_stats = char_stats(base_text)
    scores = brute_force_xor(ciphertext_bytes, base_stats, top=3)
    pprint(scores)

if __name__ == '__main__':
    main()

# Sample output
# [{'Score': 0.03191, 'Text': b'Ieeacdm*GI-y*fcao*k*ze\x7fdn*el*hkied'},
#  {'Score': 0.03203, 'Text': b"Cooking MC's like a pound of bacon"},
#  {'Score': 0.039, 'Text': b"Dhhlni`'JD t'knlb'f'whric'ha'efdhi"}]