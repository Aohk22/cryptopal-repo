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


if __name__ == '__main__':
    hdt1 = b'this is a test'
    hdt2 = b'wokka wokka!!!'
    hd_test = hamming_distance(hdt1, hdt2)
    print(hd_test)

    hds = list()
    f_ks = KEYSIZE[0]
    i = 0
    while i < len(KEYSIZE):
        n_ks = 
        hds.append