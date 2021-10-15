from typing import Pattern, List
import hashlib
import os
import re
import argparse


def md5_file(path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


CURRENT_DIR: str = os.curdir
ROOT: str = os.path.abspath(os.path.expanduser(os.path.expandvars(CURRENT_DIR)))
parser = argparse.ArgumentParser(description='Test 1')
parser.add_argument('dirs',
                    action='store',
                    nargs='+',
                    type=str,
                    help='paths to the source directories (relatively to the current directory)')
parser.add_argument('--verbose',
                    dest='verbose',
                    action='store_true',
                    help='an integer')
args = parser.parse_args()
dirs: List[str] = args.dirs
verbose: bool = args.verbose
dirs.sort()

if verbose:
    print("# Current directory: {}".format(ROOT))

pattern: Pattern = re.compile('\\.py$', re.I)
py_files: List[str] = []
for root in dirs:
    files: List[str] = [os.path.join(path, name) for path, subdirs, files in os.walk(os.path.join(CURRENT_DIR, root)) for name in files if pattern.search(name)]
    files.sort()
    if verbose:
        p = os.path.join(ROOT, root)
        print("# {}:".format(p))
        print("{}".format("\n".join(map(lambda x: "#   {}".format(x), files))))
    py_files.extend(files)
py_files.sort()

max_length = max(map(lambda x: len(x), py_files))
for file in py_files:
    print("{} {}".format(file.ljust(max_length), md5_file(file)))


signatures: List[str] = ["{}|".format(md5_file(path)) for path in py_files]
hash_md5 = hashlib.md5()
for signature in signatures:
    hash_md5.update(signature.encode())
print("{} {}".format('-' * max_length, hash_md5.hexdigest()))
