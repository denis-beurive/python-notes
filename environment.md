# Environmental data gathering

Path to the current script (<=> \_\_FILE\_\_ in C)

    import os
    os.path.abspath(__file__)

Path to the directory that contains the current script (<=> \_\_DIR_\_\ in C)

    import os
    print(os.path.dirname(os.path.abspath(__file__)))

Get an environment variable:

    import os
    print(os.environ['PATH'])