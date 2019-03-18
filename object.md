# Object

## Get all the attributes of an object

Use the builtin function `dir()`.

For example:

    import re

    class A:

        def __init__(self):
            self.pubA1  = 1
            self.pubA2  = 2
            self._prvA1 = 10
            self._prvA2 = 20

    class B(A):

        def __init__(self):
            super().__init__()
            self.pubB1 = 100
            self.pubB2 = 100

    attribute_name: str
    for attribute_name in dir(B()):
        if re.match('^__', attribute_name) is None:
            print(f' - {attribute_name}')

Result:

     - _prvA1
     - _prvA2
     - pubA1
     - pubA2
     - pubB1
     - pubB2

## Add a new attribute in an object

Use the object method `__setattr__()`.

In the following example, we add the attribute "`new_attribute`" to an object:

    import re

    class A:

        def __init__(self):
            self.pubA1  = 1
            self.pubA2  = 2
            self._prvA1 = 10
            self._prvA2 = 20

    class B(A):

        def __init__(self):
            super().__init__()
            self.pubB1 = 100
            self.pubB2 = 100

    a = A()
    a.__setattr__('new_attribute', 100)
    for attribute_name in dir(a):
        if re.match('^__', attribute_name) is None:
            print(f' - {attribute_name} => {a.__getattribute__(attribute_name)}')

Result:

     - _prvA1 => 10
     - _prvA2 => 20
     - new_attribute => 100
     - pubA1 => 1
     - pubA2 => 2

## Handy functions

    def dump_attrs(o: object):
        for name in dir(o):
            if re.match('^__', name) is None:
                print(f'- {name}: {o.__getattribute__(name)}')

