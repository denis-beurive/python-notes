# Conversions

Integer to string:

    a = 10
    print(str(a))

String to integer:

    s = '10'
    i = 2 * int(s)
    print(f'i = {i}')

Bytes to string:

    b = b'abcd'
    s = b.decode() # If the data comes from the outside, you may need to specify the encoding
    print(s)

String to bytes:

    s = 'abcd'
    ints = [ord(c) for c in s]
    b = bytes(bytearray(ints))
