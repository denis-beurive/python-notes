# Files

Load the content of a file:

    with open('/etc/hosts', 'r') as fd:
        content = fd.read()
    print(content)

Test if a file exists:

    from pathlib import Path
    path = Path('/etc/hosts')
    if path.is_file():
        print(f"{path} exists and is a file")

Copy a file:

    from shutil import copyfile
    try:
        copyfile('/etc/hosts', '/tmp/etc-hosts')
    except Exception as e:
        print(f'Cannot copy "/etc/hosts": {e}')
    else:
        print('Done')
