# Visit all entries within a data structure.

from typing import Union

d = {'a': 1,
     'b': {'aa': 11, 'bb': [0, 1, "1"]},
     'c': [{}, {'aaa': 111}]}


def walk(entry: Union[dict, list, str, int, float]) -> None:
    if isinstance(entry, dict):
        for key, value in entry.items():
            print("key: {}".format(key))
            walk(value)
        return
    if isinstance(entry, list):
        for item in entry:
            walk(item)
        return
    print("> {}".format(entry))


walk(d)
