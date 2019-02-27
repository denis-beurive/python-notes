# Operators

Ternary operator:

    a = 10
    print('a>10' if a > 10 else 'a<10')

Logical operators:

    a = 10; b=10

    if a>10 and a<20 or b==10:
        print("a>10 and a<20 or b==10")

    # same as:

    if 10<a<20 or b==10:
        print("a>10 and a<20 or b==10")

# Debug

Dump the value of a variable:

    from pprint import pprint, pformat
    lst = ['10', '11', '12', '13', '14']
    pprint(lst)
    print(pformat(lst))

Get the name of the object class:

    lst = ['10', '11', '12', '13', '14']
    print(lst.__class__.__name__)

Get the "reference/pointer" to an object:

    lst = ['10', '11', '12', '13', '14']
    print(id(lst))

# Environmental data gathering

Path to the current script (<=> __FILE__ in C)

    import os
    os.path.abspath(__file__)

Path to the directory that contains the current script (<=> __DIR__ in C)

    import os
    print(os.path.dirname(os.path.abspath(__file__)))

Get an environment variable:

    import os
    print(os.environ['PATH'])

# Arrays / Lists

Number of element in array:

    lst = ['10', '11', '12', '13', '14']
    print(len(lst)) # => 5

Test if a given value is within an array:

    lst = ['10', '11', '12', '13', '14']
    pprint('12' in lst) # => True

Join / implode:

    lst = ['10', '11', '12', '13', '14']
    print(';'.join(lst)) # => 10;11;12;13;14

Apply a transformation on all elements of an array:

    lst = [10, 11, 12, 13, 14]
    lst = map(lambda x: str(2*x), lst)
    print(';'.join(lst)) # => 10;11;12;13;14

Sort:

    lst = [10, 11, 12, 13, 14]
    lst.sort(reverse=True)
    print(';'.join(map(lambda x: str(x), lst))) # => 14;13;12;11;10

Compare:

    lst1 = [10, 11, 12, 13, 14]
    lst2 = [10, 11, 12, 13, 14]
    if lst1 == lst2:
        print("Identical!") # => Identical
        
    lst1 = [11, 12, 13, 14, 10]
    lst2 = [10, 11, 12, 13, 14]
    if lst1 != lst2:
        print("Not identical!") # Not identical

# Files

Load the content of a file:

    with open('/etc/hosts', 'r') as fd:
        content = fd.read()
    print(content)

# Serialization

    import pickle

    lst = [10, 20, 30]
    with open('list.bin', mode='wb') as fd:
        pickle.dump(lst, fd)

    with open('list.bin', mode='rb') as fd:
        lst_bin = fd.read()
    list_object = pickle.loads(lst_bin)

    print(';'.join(map(lambda x: str(x), list_object))) # 10;20;30

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

# Dictionaries

Test if a dictionary has a key:

    d = { 'a': 1, 'b': 2 }
    print('yes' if 'a' in d else 'no') # => yes

Get keys:

    d = { 'a': 1, 'b': 2 }
    ks = d.keys # ks is a function!!!
    keys = list(ks())
    print(';'.join(keys)) # => a;b

Get values:

    d = { 'a': '1', 'b': '2' }
    vs = d.values # vs is a function!!!
    values = list(vs())
    print(';'.join(values)) # => 1;2

Get couples (key, value):

    d = { 'a': '1', 'b': '2' }
    items = d.items() # items is NOT a function!!!
    print(', '.join(map(lambda x: '%s:%s'%(x[0], x[1]), items))) # => a:1, b:2

# Strings

Templates:

    street = '1 av de Paris'
    zip_code = 92110
    city = 'Clichy'

    address = Template("$street\n${zip} $city");
    s = address.substitute(street=street, zip=zip_code, city=city)
    print(s)




