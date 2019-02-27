# Environmental data gathering

Path to the current script (<=> __FILE__ in C)

    import os
    os.path.abspath(__file__)

Path to the directory that contains the current script (<=> __DIR__ in C)

    import os
    print(os.path.dirname(os.path.abspath(__file__)))

Get an environment variable:

    import os
    print(os.environ['PATH'])