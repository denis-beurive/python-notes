import re
from typing import Pattern, Match, Optional

reg1 = re.compile('abc')
reg2 = re.compile('^abc')

tests = [
    'abcd',
    '.abcd'
]

for test in tests:
    m1: Optional[Match] = reg1.match(test)
    m2: Optional[Match] = reg2.match(test)
    print(f"reg1.match('{test}') => {'matches' if m1 is not None else 'does not match.'}")
    print(f"reg2.match('{test}') => {'matches' if m1 is not None else 'does not match.'}")

# Result:
#
# reg1.match('abcd') => matches
# reg2.match('abcd') => matches
# reg1.match('.abcd') => does not match.
# reg2.match('.abcd') => does not match.
