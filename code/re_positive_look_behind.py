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


# This is positive look behind.

# (?<=a)b: "b" preceded by "a".
#
# Notes:
#
# * This expression matches **one and exactly one** character: "b".
# * An "b" that is not preceded by any character is, even more so, not preceded by a "a".

p: Pattern = re.compile('(?<=a)b')
m: Optional[Match] = p.match('b')
dump_match('[1]', m)  # Fails. "b" should not be the first character of the text.

# "b" is indeed preceded by "a".
# However, this expression matches **one and exactly one** character: "b".
# When used with "match", it implies that "b" should be the first character in the text...
# which is impossible.
p: Pattern = re.compile('(?<=a)b')
m: Optional[Match] = p.match('ab')
dump_match('[2]', m)  # Fails.

# However, using "search", it matches.
# Indeed "search" does not imply that "b" must be the first character of the text.
p: Pattern = re.compile('(?<=a)b')
m: Optional[Match] = p.search('ab')
dump_match([3], m)  # Match "b".

# We look for an "a" followed by a "b" preceded itself by an "a".
p: Pattern = re.compile('a(?<=a)b')
m: Optional[Match] = p.match('ab')
dump_match('[4]', m)  # Match "ab"

# Result:
#
#     [1] no match
#
#     [2] no match
#
#     [3] 0   : 'b'
#
#     [4] 0   : 'ab'




