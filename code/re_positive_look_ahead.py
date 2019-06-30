import re
from typing import Pattern, Match, Optional, Union, List
from pprint import pformat


def dump_match(tag: str, m: Union[Optional[Match], List[str]]):
    if m is None:
        print("{} no match\n".format(tag))
        return

    if isinstance(m, Match):
        print('{} {:<4}: {}'.format(tag, 0, pformat(m.group(0))))
        for i in range(0, len(m.groups())):
            print('{} {:<4}: {}'.format(tag, i+1, pformat(m.group(i+1))))
    else:
        if len(m) == 0:
            print("{} no match\n".format(tag))
            return
        for i in range(0, len(m)):
            print('{} {:<4}: {}'.format(tag, i, pformat(m[i])))
    print('')


# This is positive look ahead.

# a(?=b): "a" followed by "b".
#
# Notes:
#
# * This expression matches **one and exactly one** character: "a".
# * An "a" that is not followed by any character is, even more so, not followed by a "b".

p: Pattern = re.compile('a(?=b)')
m: Optional[Match] = p.match('a')
dump_match('[1]', m)  # Fails

p: Pattern = re.compile('a(?=b)')
m: Optional[Match] = p.match('abc')
dump_match('[2]', m)  # Matches "ab"

# Result:
#
#     [1] no match
#
#     [2] 0   : 'a'

