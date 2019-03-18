# Inheritance

#!/usr/bin/env python3

    from pprint import pformat

    class A:

        def __new__(cls, *args, **kwargs):
            print("[A] new(%s):\n\t* %s%s%s" %(__class__.__name__,
                                          cls.__name__,
                                          ("\n\t* *args: " if len(args) > 0 else '') + ', '.join(map(lambda x: '"%s"'%str(x), list(args))),
                                          ("\n\t* **kwargs: " if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))
            o = super(__class__, cls).__new__(cls)
            return o

        def __init__(self, *args, **kwargs):
            print('[A] %s: init(%s%s)' %(__class__.__name__,
                                        ', '.join(map(lambda x: '"%s"'%str(x), list(args))),
                                        (', ' if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))

    class B(A):

        def __new__(cls, *args, **kwargs):
            print("[B] new(%s):\n\t* %s%s%s" %(__class__.__name__,
                                           cls.__name__,
                                           ("\n\t* *args: " if len(args) > 0 else '') + ', '.join(map(lambda x: '"%s"'%str(x), list(args))),
                                           ("\n\t* **kwargs: " if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))
            o = super(__class__, cls).__new__(cls, *args, **kwargs)
            return o

        def __init__(self, *args, **kwargs):
            print('[B] %s: init(%s%s)' %(__class__.__name__,
                                        ', '.join(map(lambda x: '"%s"'%str(x), list(args))),
                                        (', ' if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))
            super().__init__(*args, **kwargs)

    class C(B):

        def __new__(cls, *args, **kwargs):
            print("[C] new(%s):\n\t* %s%s%s" %(__class__.__name__,
                                              cls.__name__,
                                              ("\n\t* *args: " if len(args) > 0 else '') + ', '.join(map(lambda x: '"%s"'%str(x), list(args))),
                                              ("\n\t* **kwargs: " if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))
            o = super(__class__, cls).__new__(cls, *args, **kwargs)
            print("%s: cls(that is: %s) is subclass of %s ? %s" %(__class__.__name__,
                                                                  cls.__name__,
                                                                  __class__.__name__,
                                                                  "true" if issubclass(cls, __class__) else "false"))
            return o

        def __init__(self, *args, **kwargs):
            print('[C] %s: init(%s%s)' %(__class__.__name__,
                                    ', '.join(map(lambda x: f'"%s"'%str(x), list(args))),
                                    (', ' if len(kwargs) > 0 else '') + ', '.join(map(lambda x: '%s="%s"'%(str(x[0]), str(x[1])), kwargs.items()))))
            super().__init__(*args, **kwargs)


    print('-------------------------------------')
    A = A(1, 2, 3, name='This is A')
    print('')
    print('-------------------------------------')
    b = B(1, 2, 3, name='This is B')
    print('')
    print('-------------------------------------')
    c = C(1, 2, 3, name='This is C')
    print('')
    print('-------------------------------------')

Result:

    -------------------------------------
    [A] new(A):
            * A
            * *args: "1", "2", "3"
            * **kwargs: name="This is A"
    [A] A: init("1", "2", "3", name="This is A")

    -------------------------------------
    [B] new(B):
            * B
            * *args: "1", "2", "3"
            * **kwargs: name="This is B"
    [A] new(A):
            * B
            * *args: "1", "2", "3"
            * **kwargs: name="This is B"
    [B] B: init("1", "2", "3", name="This is B")
    [A] A: init("1", "2", "3", name="This is B")

    -------------------------------------
    [C] new(C):
            * C
            * *args: "1", "2", "3"
            * **kwargs: name="This is C"
    [B] new(B):
            * C
            * *args: "1", "2", "3"
            * **kwargs: name="This is C"
    [A] new(A):
            * C
            * *args: "1", "2", "3"
            * **kwargs: name="This is C"
    C: cls(that is: C) is subclass of C ? true
    [C] C: init("1", "2", "3", name="This is C")
    [B] B: init("1", "2", "3", name="This is C")
    [A] A: init("1", "2", "3", name="This is C")

    -------------------------------------


