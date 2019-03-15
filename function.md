# Function

## Arguments

Example:

    def outer(v1, *criteria, p1, p2, **kwargs):
        print(f'outer:       v1 = {v1}')
        print(f'       criteria = {pformat(criteria)}')
        print(f'             p1 = {p1}')
        print(f'             p2 = {p2}')
        print(f'         kwargs = {pformat(kwargs)}')
        inner(*criteria, p1=p1, p2=p2)

    def inner(*criteria, p1, p2, p3=1000, **kwargs):
        print(f'inner: criteria = {pformat(criteria)}')
        print(f'             p1 = {p1}')
        print(f'             p2 = {p2}')
        print(f'             p3 = {p3}')
        print(f'         kwargs = {pformat(kwargs)}')

    params = [1, 2]
    print(f'params = {pformat(params)}')
    outer('a', *params, p1=100, p2=200, option='o')

In this example:

* **outer**:
    * **`v1`**: first mandatory positional argument.
    * **`criteria`**: hold zero or more optional positional arguments.
    * **`p1`** and **`p2`**: mandotory named arguments.
    * **`kwargs`**: hold zero or more optional named arguments.
* **inner**:
    * **`criteria`**: hold zero or more optional positional arguments.
    * **`p1`** and **`p2`**: mandotory named arguments.
    * **`p3`**: optional named arguments.
    * **`kwargs`**: hold zero or more optional named arguments.

Result:

    params = [1, 2]
    outer:       v1 = a
           criteria = (1, 2)
                 p1 = 100
                 p2 = 200
             kwargs = {'option': 'o'}
    inner: criteria = (1, 2)
                 p1 = 100
                 p2 = 200
                 p3 = 1000
             kwargs = {}

## Inner functions

    def outer_function():

        def inner_function():
            print('This is inner_function')

        inner_function()

    outer_function() # => This is inner_function

## Functions names are variables

    def f():
        print('This is f')

    def g():
        print('This is g')

    def h():
        return g

    f()   # => This is f
    g()   # => This is g
    f=h()
    f()   # => This is g

## Function composition

See [Function composition](https://en.wikipedia.org/wiki/Function_composition)

    from typing import Callable

    def f(x: int) -> int:
        return 2*x

    def g(x: int) -> int:
        return x+3

    def composition(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:

        def fog(x: int) -> int:
            return f(g(x))

        return fog

    # h(x) = 2*(x+3)
    h = composition(f, g)
    # h(3) = 2*(3+3) = 12
    print(f'fog(3) = {h(3)}') # => fog(3) = 12

## Function composition => decorators!

    from typing import Callable

    def f(function: Callable[[int], int]) -> Callable[[int], int]:
        return lambda x: 2*function(x)

    @f
    def g(x: int) -> int:
        return x+3

    print(f'fog(3) = {g(3)}') # fog(3) = 12





