# Type checkings

## Checking that an object is of a given type

String:

    s = 'abc'
    if isinstance(s, str):
        print('s in a string')
    if isinstance(s, collections.Sequence):
        print('s in a collections.Sequence')

Dictionary:

    o = {'a':1}
    if isinstance(o, dict):
        print('o is a dictionary')
    if isinstance(o, collections.Mapping):
        print('o is a collections.Mapping')

List:

    o = [1]
    if isinstance(o, list):
        print('o is a list')
    if isinstance(o, collections.Sequence):
        print('o is a collections.Sequence')

Tuple:

    o = (1, 2)
    if isinstance(o, tuple):
        print('o is a tuple')
    if isinstance(o, collections.Sequence):
        print('o is a collections.Sequence')

Set:

    colors = {'red', 'green', 'blue'}
    if isinstance(colors, set):
        print('colors is a set')
    if isinstance(colors, collections.Set):
        print('colors is a collections.Set')

Functions:

    f1 = lambda x: 2*x
    if callable(f1):
        print('f1 is a callable')
    if isinstance(f1, types.FunctionType):
        print('f1 is a types.FunctionType')

    def f2():
        pass

    if callable(f2):
        print('f2 is a callable')
    if isinstance(f2, types.FunctionType):
        print('f2 is a types.FunctionType')

Class and methods:

    class MyObject:
        def m(self):
            pass
        pass

    o = MyObject()
    if isinstance(o, MyObject):
        print('o is an instance of MyObject')
    if callable(o.m):
        print('o.m is a callable')

