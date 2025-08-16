import sys
import base64

def hex_to_b64(hex_str: str) -> bytes:
    hex_bytes = bytes.fromhex(hex_str)
    hex_b64 = base64.b64encode(hex_bytes)
    return hex_b64

def test():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    return hex_to_b64(hex_str).decode() == result

def main():
    print(test())

if __name__ == '__main__':
    main()