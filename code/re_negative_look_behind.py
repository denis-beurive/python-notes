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


# This is negative look behind.

# This may match:
p: Pattern = re.compile('^[^a](?<!a)b$')
m: Optional[Match] = p.match('cb')
dump_match('[1]', m)

# This will match only one text: "b".
#
# Why ?
#
# Because the text that matches the expression must *start* with the character "b" (that, incidentally, is not
# preceded by an "a"). Yet if "b" is preceded by a character (other than "a"), then, clearly, the text is, at least, 2
# characters long!
#
# However, "b" does not need to be preceded by a character to match the expression: if "b" is not preceded by a
# character, then it is not preceded by "a", right ? Thus, the only text that matches the expression is "b".

p: Pattern = re.compile('^(?<!a)b$')
m: Optional[Match] = p.match('cb')  # Won't match
dump_match('[2]', m)
m: Optional[Match] = p.match('b')  # Match
dump_match('[3]', m)

# However, "search" and "replace" may found matches
p: Pattern = re.compile('(?<!a)b')
r: List[str] = p.findall('cb')
dump_match('[4]', r)
p: Pattern = re.compile('(?<!a)b')
m: Optional[Match] = p.search('cb')
dump_match('[5]', r)

# This may match:
p: Pattern = re.compile('^(.)(?<!a)b$')
m: Optional[Match] = p.match('cb')
dump_match('[6]', m)

# This may match:
p: Pattern = re.compile('^([^\\d])(?<!\\d)b$')
m: Optional[Match] = p.match('cb')
dump_match('[7]', m)

# This may match:
p: Pattern = re.compile('^([^\\d])(?<!\\d)b$')
m: Optional[Match] = p.match('cb')
dump_match('[8]', m)

# This may match:
p: Pattern = re.compile('^([^\\d])(?<!\\d)b$')
m: Optional[Match] = p.match('cb')
dump_match('[9]', m)

# This may match:
p: Pattern = re.compile('^(.+)(?<!en)b$')
m: Optional[Match] = p.match('cb')
dump_match('[10]', m)

# This may match:
p: Pattern = re.compile('^(.+)(?<!en)b$')
m: Optional[Match] = p.match('aaaaab')
dump_match('[11]', m)


