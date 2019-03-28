# Strings

## HereDoc

Very simple:

    message = """
    This is
    a multiline
    string
    """

If you want to get rid of the first and last return carriage:

    message = """\
    This is
    a multiline
    string\
    """

## Templates

    street = '1 av de Paris'
    zip_code = 92110
    city = 'Clichy'

    address = Template("$street\n${zip} $city");
    s = address.substitute(street=street, zip=zip_code, city=city)
    print(s)

## Split a string

Splitting based on a simple string:

    tokens = 'a b c d'.split(' ')
    print(','.join(tokens)) # => a,b,c,d

Splitting based on a regular expression:

    import re
    from pprint import pprint

    text = 'AB;CDE;FGH;J;1 2  3   4'
    tokens = re.split('(;|\s+)', text)

    # Details, just to make things easier to see.
    pprint(tokens) # => ['AB', ';', 'CDE', ';', 'FGH', ';', 'J', ';', '1', ' ', '2', '  ', '3', '   ', '4']
    print('len(tokens) = %d' %len(tokens)) # => len(tokens) = 15
    pprint(range(0, len(tokens), 2)) # [0, 2, 4, 6, 8, 10, 12, 14]

    print('|'.join([tokens[i] for i in range(0, len(tokens), 2)])) # => AB|CDE|FGH|J|1|2|3|4

## Search and replace using a regexp

    import re
    print(re.sub(' +', ' ', '1   3   5   7')) # => 1 3 5 7

## Slicing

    text = ''.join(map(lambda x: chr(x), range(65, 65+26))) # => ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(text[0:3]) # => ABC
    print(text[:3])  # => ABC
    print(text[3:])  # => DEFGHIJKLMNOPQRSTUVWXYZ

## The operator *

    text = 'x' * 3
    print(text) # => xxx

## Finding the maximum length of a list of strings

Example 1:

    m: int = max(map(lambda x: len(x), ['1', '22', '333']))
    print(f"Max length: {m}\n")

Example 2:

    cities = {
        "Paris": "France",
        "Madrid": "Spain",
        "New-York": "U.S"
    }

    m: int = max(map(lambda x: len(x), cities.keys()))
    print(f"Max length: {m}\n")

    for name, value in cities.items():
        print('* {:<{width}}: {}'.format(name, value, width=m))

## Formatting

Very good link: [PyFormat](https://pyformat.info/)

### `__str__` vs `__repr__`

    from typing import List

    class Data:

        def __init__(self, value: List[int]):
            self._data = value

        def __str__(self):
            return '[' + ', '.join(map(lambda x: f'<{str(x)}>', self._data)) + ']'

        def __repr__(self):
            return 'Data(' + ', '.join(map(lambda x: f'<{str(x)}>', self._data)) + ')'

    d = Data([2, 4, 6])

    # !s call __str__
    # !r call __repr__

    print("{!s}\n{!r}".format(d, d))

Result:

    [<2>, <4>, <6>]
    Data(<2>, <4>, <6>

### Align left, rigth, center

    print('[{:>5}]'.format('x'))
    print('[{:<5}]'.format('x'))
    print('[{:^5}]'.format('x'))

    print('[{:->5}]'.format('x'))
    print('[{:-<5}]'.format('x'))
    print('[{:-^5}]'.format('x'))

Result:

    [    x]
    [x    ]
    [  x  ]
    [----x]
    [x----]
    [--x--]

### Truncating

    print('{:.3}'.format('abcdef')) # => abc

Truncating can be mixed with the alignment:

    print('{:-^11.3}'.format('abcdef')) # => ----abc----

### Named placeholders

    print('{a} {b}'.format(a=10, b=20)) # => 10 20
    data = {'a':40, 'b':80}
    print('{a} {b}'.format(**data)) # => 40 80

### Parametrized formats

This can be very handy:

    print('[{:{fill}{align}{width}}]'.format('x', fill='-', align='^', width='9'))

Result:

    [----x----]


