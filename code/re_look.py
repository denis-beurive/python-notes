from typing import Optional, Pattern, Match
import re


def match_status(m: Optional[Match]) -> str:
    return m.group(0) if m is not None else "no match"


# Positive look-ahead: "a" is followed by "b".
# ab => a
# a => no match

print("Positive look-ahead: a(?=b) ('a' followed by 'b')")
p: Pattern = re.compile('a(?=b)')
texts = ['ab', 'a']
for text in texts:
    m: Optional[Match] = p.search(text)
    print(f'{text} => {match_status(m)}')
print('')

# Negative look-ahead: "a" is not followed by "b".
# ax => a
# a => a

print("Negative look-ahead: a(?!b) ('a' not followed by 'b')")
p: Pattern = re.compile('a(?!b)')
texts = ['ax', 'a']
for text in texts:
    m: Optional[Match] = p.match(text)
    print(f'{text} => {match_status(m)}')
print('')

# Positive look-behind: "b" is preceded by "a".
# ab => b
# a => no match

print("Positive look-behind: (?<=a)b ('b' preceded by 'a')")
p: Pattern = re.compile('(?<=a)b')
texts = ['ab', 'a']
for text in texts:
    m: Optional[Match] = p.search(text)
    print(f'{text} => {match_status(m)}')  # => b
print('')

# Negative look-behind: "b" is not preceded by "a".
# xb => b
# b => b

print("Negative look-behind: (?<!a)b ('b' not preceded by 'a')")
p: Pattern = re.compile('(?<!a)b')
texts = ['xb', 'b']
for text in texts:
    m: Optional[Match] = p.search(text)
    print(f'{text} => {match_status(m)}')  # => b
print('')



