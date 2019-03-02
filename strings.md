# Strings

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

## Slicing

    text = ''.join(map(lambda x: chr(x), range(65, 65+26))) # => ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(text[0:3]) # => ABC
    print(text[:3])  # => ABC
    print(text[3:])  # => DEFGHIJKLMNOPQRSTUVWXYZ




