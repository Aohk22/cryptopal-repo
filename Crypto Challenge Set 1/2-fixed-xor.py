def fixed_xor(str1: str, str2: str) -> bytes:
    bstr1 = bytes.fromhex(str1)
    bstr2 = bytes.fromhex(str2)
    return b''.join([bytes([b1 ^ b2]) for b1, b2 in zip(bstr1, bstr2)])

def test():
    str1 = '1c0111001f010100061a024b53535009181c'
    str2 = '686974207468652062756c6c277320657965'
    result = '746865206b696420646f6e277420706c6179'
    xor_result = fixed_xor(str1, str2).hex()
    return xor_result == result

def main():
    print(test())

if __name__ == '__main__':
    main()