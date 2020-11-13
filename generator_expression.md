# Generator expression

See [PEP 289 -- Generator Expressions](https://www.python.org/dev/peps/pep-0289/)

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


# Using yield

Write a generator that takes 2 parameters:
* a value `x`
* a function `f(x)`

The generator must return: `x`, `f(x)`, `f(f(x))`, `f(f(f(x)))`... 


    import typing
    
    # x, f(x), f(f(x)), f(f(f(x)))...
    def fgen(f: typing.Callable[[typing.Any], typing.Any], x: typing.Any) \
            -> typing.Generator[typing.Any, None, None]:
        while True:
            yield x
            x = f(x)
    
    
    # Expected: 3, 2*3, 2*2*3, 2*2*2*3
    for counter, value in enumerate(fgen(lambda x: 2*x, 3)):
        print(f"{counter:d}: {value:d}")


