# Named tuples

    from typing import NamedTuple
    from collections import namedtuple, Iterable, Mapping

    data: NamedTuple = namedtuple('Color', 'red green blue')
    data.red = 0
    data.green = 10
    data.blue = 20
    print(data.__class__.__name__) # => type

    print(f'data is {"" if isinstance(data, Iterable) else "NOT"} iterable.')

    print(f'data is {"" if isinstance(data, Mapping) else "NOT"} a Mapping.')

Result:

    type
    data is NOT iterable.
    data is NOT a Mapping.
