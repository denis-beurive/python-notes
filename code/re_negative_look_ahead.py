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

# The only text that matches is "a".
#
# Why ?
#
# Because the text that matches the expression must *start* with the character "a" (that, incidentally, is not
# followed by a "b"). Yet if "a" is followed by a character (other than "b"), then, clearly, the text is, at least, 2
# characters long!
#
# However, "a" does not necessarily need to be followed by a character. If "a" is not followed by any character, then is
# it not followed by "b", right ? Thus, the only text that matches the expression is "a".
p: Pattern = re.compile('^a(?!b)$')
m: Optional[Match] = p.match('a')
dump_match('[1]', m)

# However, "search" and "replace" may found matches
p: Pattern = re.compile('a(?!b)')
m: Optional[Match] = p.search('-aaab')
dump_match('[2]', m)  # Found 1 match (the first "a")
r: List[str] = p.findall('aaab')
dump_match('[3]', r)  # Found 2 matches (the 2 first "a")

# This may match, since the text that matches must be 2 characters long.
p: Pattern = re.compile('^a(?!b).$')
m: Optional[Match] = p.match('ac')
dump_match('[4]', m)  # Match
p: Pattern = re.compile('^a(?!b)(.+)$')
m: Optional[Match] = p.match('acxx')
dump_match('[5]', m)  # Match

# This may also match.
p: Pattern = re.compile('^a(?!xx)..$')
m: Optional[Match] = p.match('a--')
dump_match('[6]', m)  # Match
m: Optional[Match] = p.match('ax-')
dump_match('[7]', m)  # Match
