# Generator expression

    from typing import Generator, List

    r: List = [x for x in range(0, 10)]
    print(f'r is a {r.__class__.__name__}') # => list

    r: Generator = (x for x in range(0, 3))
    print(f'r is a {r.__class__.__name__}') # => generator

    print('')
    for i in r:
        print(i)

    print('')
    r: Generator = (x for x in range(0, 3))
    while True:
        try:
            print(next(r))
        except StopIteration:
            break

    print('')
    r = list((x for x in range(0, 10)))
    print(f't is a {r.__class__.__name__}') # => list

Result:

    r is a list
    r is a generator

    0
    1
    2

    0
    1
    2

    t is a list

