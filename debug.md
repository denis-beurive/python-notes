# Debug

Dump the value of a variable:

    from pprint import pprint, pformat
    lst = ['10', '11', '12', '13', '14']
    pprint(lst)
    print(pformat(lst))

Get the name of the object class:

    lst = ['10', '11', '12', '13', '14']
    print(lst.__class__.__name__)

Get the "reference/pointer" to an object:

    lst = ['10', '11', '12', '13', '14']
    print(id(lst))