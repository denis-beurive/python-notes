import re
from typing import Pattern, Match, Optional


text: str = """a@b
c@d
this is some more text.
"""

# Be aware that "\s" includes "\n"!

# The option MULTILINE is not set.
# However, the search for a match spans upon several lines.

p: Pattern = re.compile('(\\w+@\\w+)\\s*(\\w+@\\w+)\\s*')
m: Optional[Match] = p.match(text)
print(m.group(1))  # => a@b
print(m.group(2))  # => c@d
print('')

# The option MULTILINE is set.
# However, the expression matches only one expression.

p: Pattern = re.compile('(\\w+@\\w+)', re.MULTILINE)
m: Optional[Match] = p.match(text)
print(f'{m.group(1)} {len(m.groups())}')  # => a@b (1)

# Result:
#
#     a@b
#     c@d
#
#     a@b 1
