# Sorting

The following example shows how to use a special comparison function to sort objects.

> See the function [functools.cmp_to_key](https://docs.python.org/3.5/library/functools.html).

    import sys
    from packaging.version import Version
    from typing import List
    from pprint import pprint
    import functools

    def cmp_version(v1: Version, v2: Version) -> int:
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0

    cmp = functools.cmp_to_key(cmp_version)

    versions: List[Version] = list(map(lambda x: Version(x), sys.argv[1:]))
    versions.sort(key=cmp)
    pprint(versions.pop().__str__())

