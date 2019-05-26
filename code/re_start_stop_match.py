import re
from typing import Pattern, Match, Optional, List
from pprint import pformat


# The following expression matches a single "virtual line" that may span over several "physical" lines.
#
# Example of a "virtual lines":
#
#   abc\
#   def\
#   ghi
#   jkl
#
# This text contains 2 virtual lines:
#
#   abc\
#   def\
#   ghi
#
# And:
#
#   jkl

ml: Pattern = re.compile('^((?:(?:\\\\\\n)|[^\\n])+)\\n?(.*)')

texts: List[str] = [
    ">>> abc",
    "\n".join([
        '>>> abc',
        'end'
    ]),
    "\n".join([
        '>>> abc \\',
        '    def \\',
        '    ghi',
        'end'
    ])
]

i = 1
for text in texts:
    print(f'> {i}: {pformat(text)}')
    m: Optional[Match] = ml.match(text)
    if m is None:
        print("No match\n")
        continue
    for t in m.groups():
        s = re.sub('\\s*\\\\\\n\\s*', ' ', t)
        print(pformat(s))
    print('')
    i += 1

# Result:
#
#     > 1: '>>> abc'
#     '>>> abc'
#     ''
#
#     > 2: '>>> abc\nend'
#     '>>> abc'
#     'end'
#
#     > 3: '>>> abc \\\n    def \\\n    ghi\nend'
#     '>>> abc def ghi'
#     'end'
