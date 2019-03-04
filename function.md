# Function

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

* **`v1`**: first mandatory positional argument.
* **`criteria`**: hold zero or more optional positional arguments.
* **`p1`** and **`p2`**: mandotory named arguments.
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

