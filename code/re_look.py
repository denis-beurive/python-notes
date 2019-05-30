from typing import Optional, Pattern, Match
import re
 
print("Positive look-ahead: a(?:b) ('a' followed by 'b')")
p: Pattern = re.compile('a(?:b)')
text: str = 'abc'
m: Optional[Match] = p.search(text)
print(f'{text} => {m.group(0)}')  # => ab
print('')
 
# Negative look-ahead: "a" is not followed by "b".
 
print("Negative look-ahead: a(?!b) ('a' not followed by 'b')")
p: Pattern = re.compile('a(?!b)')
text: str = 'ax'
m: Optional[Match] = p.match(text)
print(f'{text} => {m.group(0)}')  # => a
print('')
 
# Negative look-behind: "b" is not preceded by "a".
 
print("Negative look-behind: (?<!a)b ('b' not preceded by 'a')")
p: Pattern = re.compile('(?<!a)b')
text: str = 'xb'
m: Optional[Match] = p.search(text)
print(f'{text} => {m.group(0)}')  # => b
print('')
 
# Positive look-behind: "b" is preceded by "a".
 
print("Positive look-behind: (?<=a)b ('b' preceded by 'a')")
p: Pattern = re.compile('(?<=a)b')
text: str = 'ab'
m: Optional[Match] = p.search(text)
print(f'{text} => {m.group(0)}')  # => b
print('')