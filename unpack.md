# Unpack / Splat

## With lists

ex1:

    one, two, third = [1, 2, 3]
    print(f'{one} {two} {third}') # => 1 2 3

ex2:

    *first_three, fourth = [1, 2, 3, 4]
    print(','.join(map(lambda x: str(x), first_three))) # => 1,2
    print(f'... and {fourth}')

ex3:

    *first_two, third, fourth = [1, 2, 3, 4]
    print(','.join(map(lambda x: str(x), first_two))) # => 1,2
    print(f'... and {third}')
    print(f'... and {fourth}')

ex4:

    first, *the_test = [1, 2, 3, 4]
    print(f'{first}')
    print('... and ' + ','.join(map(lambda x: str(x), the_test))) # => 1,2

ex5:

    def f(p1, p2):
        print(f'{str(p1)}, {str(p2)}')

    v = [10, 20]
    f(*v) # => 10, 30 

ex6:

    def f(*args):
        print(f'{len(args)}: ' + ','.join(map(lambda x: str(x), args)))

    f(*[10, 20, 30]) # => 3: 10,20,30
    f(100, 200, 300) # => 3: 100,200,300

ex7:

    def outer(*criteria):
        print(f'outer:  criteria      = {pformat(criteria)}')
        print(f'        len(criteria) = {len(criteria)}')
        print(f'        criteria[0]   = {pformat(criteria[0])}')
        inner(*criteria, 10)

    def inner(*criteria):
        print(f'inner:  criteria = {pformat(criteria)}')

    params = [10, 20, 30]
    print(f'params = {pformat(params)}')
    outer(*params)

Reasul:

    params = [10, 20, 30]
    outer:  criteria      = (10, 20, 30)
            len(criteria) = 3
            criteria[0]   = 10
    inner:  criteria = (10, 20, 30, 10)
    
## With dictionaries

Watch out! The dictionary behaves like a list!

    *f, r = {'k1': 10, 'k2': 20, 'k3': 30}
    pprint(f) # => ['k1', 'k2']
    pprint(r) # => 'k3'

The function parameters are correctly assigned:

    def f(p1, p2):
        print(f'{str(p1)}, {str(p2)}')

    d = {'p2': 'param2', 'p1': 'param1'}
    f(**d) # => param1, param2
    f(p2='param2', p1='param1') # => param1, param2

or:

    def ff(**kwargs):
        print(f'{kwargs["p1"]} {kwargs["p2"]} {kwargs["p3"]}')

    params = {'p1': 10, 'p2': 20, 'p3': 30}
    ff(**params) # => 10 20 30
    ff(p1=10, p2=200, p3=3000) # => 10 200 3000

