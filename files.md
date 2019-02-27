# Files

Load the content of a file:

    with open('/etc/hosts', 'r') as fd:
        content = fd.read()
    print(content)

