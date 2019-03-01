# Directories

Build a path to a file

    print(os.path.join('/', 'path', 'to', 'the', 'file')) # => /path/to/the/file

Test if a path points to a directory

    import os
    if os.path.isdir('.'):
        print('"." points to a directory!')

List all the files within a directory

    import os
    dir_path = '.'
    files = []
    for entry in os.listdir(dir_path):
        if not os.path.isfile(os.path.join(dir_path, entry)):
            continue
        files.append(entry)
    print("\n".join(files))

