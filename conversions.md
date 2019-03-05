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

Map opject to list:

    r = map(lambda x: 2*x, [1, 3])
    print(r.__class__.__name__) # => map

    r: List[int] = list(map(lambda x: 2*x, [1, 3]))
    pprint(r) # => [2, 6]

Generator to list:

    from typing import Generator, List

    r: Generator = (x for x in range(0, 10))
    print(r.__class__.__name__) # => generator

    r = list((x for x in range(0, 10)))
    print(r.__class__.__name__) # => list

    