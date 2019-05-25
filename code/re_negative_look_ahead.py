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


# This is negative look ahead.

# a(?!b): "a" not followed by "b".
#
# Notes:
#
# * This expression matches **one and only one** character: an "a".
# * An "a" that is not followed by any character is, even more so, not followed by a "b".

# One "a" not followed by a "b".
p: Pattern = re.compile('a(?!b)')
m: Optional[Match] = p.match('a')
dump_match('[1]', m)  # Match

# One "a" not followed by a "b" <=> '^a$'.
p: Pattern = re.compile('^a(?!b)$')
m: Optional[Match] = p.match('a')
dump_match('[2]', m)  # Match

# Matches the "a".
p: Pattern = re.compile('a(?!b)')
m: Optional[Match] = p.match('ac')
dump_match('[3]', m)  # Match

# "a" is not the last character <=> 'a$'
p: Pattern = re.compile('a(?!b)$')
m: Optional[Match] = p.match('ac')
dump_match('[4]', m)  # Fail

# Matches 2 characters.
p: Pattern = re.compile('a(?!b).')
m: Optional[Match] = p.match('ac')
dump_match('[5]', m)  # Match

# Matches 2 characters.
p: Pattern = re.compile('^a(?!b).$')
m: Optional[Match] = p.match('ac')
dump_match('[6]', m)  # Match

# Result:
#
#     [1] 0   : 'a'
#
#     [2] 0   : 'a'
#
#     [3] 0   : 'a'
#
#     [4] no match
#
#     [5] 0   : 'ac'
#
#     [6] 0   : 'ac'
