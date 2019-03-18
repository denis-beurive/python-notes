# Base64

Example:

    import re
    import base64

    def encode_string(s: str) -> str:
        m: bytes = base64.encodebytes(bytes(bytearray([ord(c) for c in s])))
        s = m.decode()
        s = re.sub('\n$', '', s)
        return s

    def decode_string(s: str) -> str:
        s = f"{s}\n"
        m: bytes = base64.decodebytes(bytes(bytearray([ord(c) for c in s])))
        return m.decode()


    text = 'azerty'
    encoded = encode_string(text)
    decoded = decode_string(encoded)
    assert(decoded == text)

    print(f'{len(encoded)}: [{encoded}]')
    print(f'{len(decoded)}: [{decoded}]')

Result:

    8: [YXplcnR5]
    6: [azerty]

