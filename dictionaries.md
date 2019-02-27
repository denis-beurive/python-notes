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