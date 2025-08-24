def repeat_xor(pt: bytes, k: bytes) -> bytes:
    assert len(k) <= len(pt)
    k_padded = k * (len(pt)//len(k)) + k[:(len(pt) % len(k))]
    return b''.join(bytes([a ^ b]) for a, b in zip(pt, k_padded))

if __name__ == '__main__':
    pt = b'''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
    k = b'ICE'
    answer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    ct = repeat_xor(pt, k)
    print(f'{ct.hex() == answer=}')