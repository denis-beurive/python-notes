# Arrays / Lists

Number of element in array:

    lst = ['10', '11', '12', '13', '14']
    print(len(lst)) # => 5

Test if a given value is within an array:

    lst = ['10', '11', '12', '13', '14']
    pprint('12' in lst) # => True

Join / implode:

    lst = ['10', '11', '12', '13', '14']
    print(';'.join(lst)) # => 10;11;12;13;14

Apply a transformation on all elements of an array:

    lst = [10, 11, 12, 13, 14]
    lst = map(lambda x: str(2*x), lst)
    print(';'.join(lst)) # => 10;11;12;13;14

Sort:

    lst = [10, 11, 12, 13, 14]
    lst.sort(reverse=True)
    print(';'.join(map(lambda x: str(x), lst))) # => 14;13;12;11;10

Compare:

    lst1 = [10, 11, 12, 13, 14]
    lst2 = [10, 11, 12, 13, 14]
    if lst1 == lst2:
        print("Identical!") # => Identical
        
    lst1 = [11, 12, 13, 14, 10]
    lst2 = [10, 11, 12, 13, 14]
    if lst1 != lst2:
        print("Not identical!") # Not identical