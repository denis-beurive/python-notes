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

# * ?:\\\\\\n: the string "\\\n".
# * [^\\n]: any character, except the character "newline" ("\n").
# * ((?:\\\\\\n)|[^\\n]): any character, except the character "newline" ("\n"),
#                         or the string "\\\n".
#                         -> That is; a "virtual line".
#
# Then consider (...)\\n?(.*):
#
# The "virtual line" (first capturing parentheses) stops when we hit a character
# "newline". The second capturing parentheses will contain the remaining text.


ml: Pattern = re.compile('^((?:(?:\\\\\\n)|[^\\n])+)\\n?(.*)')

texts: List[str] = [
    # Test 1
    ">>> abc",

    # Test 2:
    "\n".join([
        '>>> abc',
        'end'
    ]),

    # Test 3:
    "\n".join([
        '>>> abc \\',
        '    def \\',
        '    ghi',
        'end'
    ])
]

i = 1
for text in texts:
    print(f"### Test {i} ###\n\n{pformat(text)}\n")
    m: Optional[Match] = ml.match(text)
    print("Result:\n")
    if m is None:
        print("No match\n")
        continue
    for t in m.groups():
        # We strip the white spaces.
        s = re.sub('\\s*\\\\\\n\\s*', ' ', t)
        print(pformat(s))
    print('')
    i += 1

# Result:
#
# ### Test 1 ###
#
# '>>> abc'
#
# Result:
#
# '>>> abc'
# ''
#
# ### Test 2 ###
#
# '>>> abc\nend'
#
# Result:
#
# '>>> abc'
# 'end'
#
# ### Test 3 ###
#
# '>>> abc \\\n    def \\\n    ghi\nend'
#
# Result:
#
# '>>> abc def ghi'
# 'end'
