# Comprehensions

## List

Simple list:

    l = [ str(e*e) for e in range(0, 10) if e%2 == 0 ]
    print(','.join(l)) # => 0,4,16,36,64

    # Which should be written:

    l = [ str(e*e) for e in range(0, 10, 2) ]
    print(','.join(l)) # => 0,4,16,36,64

List of lists:

    from pprint import pprint
    l = [ [e for e in range(2*f, 2*f+3)] for f in range(0, 3) ]
    pprint(l) # => [[0, 1, 2], [2, 3, 4], [4, 5, 6]]

# Dictionaries

Simple dictionary:

    from pprint import pprint
    d = { char: chr(char) for char in range(65, 65+3) }
    pprint(d) # => {65: 'A', 66: 'B', 67: 'C'}

Dictionary of dictionary:

    from pprint import pprint
    
    d = { color: { k: f'{color}-{k}' for k in [2, 4, 6] } for color in ['R', 'G', 'B'] }
    pprint(d)

    # {'B': {2: 'B-2', 4: 'B-4', 6: 'B-6'},
    #  'G': {2: 'G-2', 4: 'G-4', 6: 'G-6'},
    #  'R': {2: 'R-2', 4: 'R-4', 6: 'R-6'}}

