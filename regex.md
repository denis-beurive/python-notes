# Regular expression

# Basics

Find all texts that match a given expression:

    import re
    from typing import Pattern

    text = "a abc bcd cde Aaa fff\na1 a2 sss"
    regex: Pattern = re.compile('a[^ ]*', re.I)
    list_of_matches = regex.findall(text)
    print(','.join(list_of_matches)) # => a,abc,Aaa,a1,a2

Test if a texts matches an expression:

    import re
    from typing import Pattern, Match, Optional

    text = 'User@Domain.com'
    regex: Pattern = re.compile('^([a-z]+)@([a-z]+\.[a-z]+)$', re.I)
    m: Optional[Match] = regex.match(text)
    if m is not None:
        print('"%s" matches!' %text)
        print(m.group(0)) # => User@Domain.com
        print(m.group(1)) # => User
        print(m.group(2)) # => Domain.com

## Using options

Multiple lines:

    # "\s" is equivalent to "[\t\n\r\f\v]".
    p: Pattern = re.compile('\\s*(\\w+@\\w+)\\s*(\\w+@\\w+)\\s*', re.MULTILINE)

    text: str = """
    a@b
    c@d
    this is some more text.
    """

    m: Optional[Match] = p.match(text)
    print(m.group(1))  # => a@b
    print(m.group(2))  # => c@d

Case insensitive:

    p: Pattern = re.compile("(\\w+)", re.IGNORECASE)
    m: Optional[Match] = p.match('abc')
    print(m.group(1))  # => abc
    m: Optional[Match] = p.match('ABC')
    print(m.group(1))  # => ABC

Multiple lines & Case insensitive:

    Multiline and case insensitive
    p: Pattern = re.compile('\\s*(\\w+)\\s*(\\w+)', re.MULTILINE | re.IGNORECASE)

    text = """
    abc
    DEF
    """

    m: Optional[Match] = p.match(text)
    print(m.group(1))  # => a@b
    print(m.group(2))  # => c@d


# Negative/Positive look ahead/behind

The basics:

* look-ahead  => followed by...
* look-behind => preceded by...

Then:

* Positive look-ahead  => followed by...
* Positive look-behind => preceded by...
* Negative look-ahead  => not followed by...
* Negative look-behind => not preceded by...

## Negative look-ahead

See full example [here](code/re_negative_look_ahead.py)

Look for "a" _not_ followed by "b":
    
    a(?!b)

Please note:

* This expression matches **one and only one** character: an "a".
* An "a" that is not followed by any character is, even more so, not followed by a "b".

Thus:

    * `match('a(?!b)', 'a')` matches (one "a" not followed by a "b").
    * `match('^a(?!b)$', 'a')` matches (only one character).
       This is aquivalent to `^a$`.
    * `match('a(?!b)', 'ac')` matches (one "a").
    * `match('a(?!b)$', 'ac')` fails ("a" is not the last character).
      This is aquivalent to `a$`.
    * `match('a(?!b).', 'ac')` matches 2 characters.
    * `match('^a(?!b).$', 'ac')` matches 2 characters.
    
> `a(?!b).` is not equivalent to `a(?!b)[^b]`. `[^b]` matches `\n` while `.` (by default) does not.

## Positive look-ahea

See full example [here](code/re_positive_look_ahead.py)

Look for "a" followed by "b":

    a(?:b)

Please note:

* This expression matches **two and exactly two** characters: "ab".
* An "a" that is not followed by any character is, even more so, not followed by a "b".

Thus:

* `match('a(?:b)', 'a')` fails (We are looking for 2 characters).
* `match('a(?:b)', 'abc')` matches "ab".

## Negative look-behind

Code [here](code/re_negative_look_behind.py)

Look for "a" _not_ preceded by "b":
    
    (?<!a)b

Please note:

* This expression matches **one and only one** character: a "b".
* A "b" that is not preceded by any character is, even more so, not preceded by a "a".

Thus:

* `match('(?<!a)b', 'cb')` fails (we are looking for a "b" at the begining of the text).
* `search('(?<!a)b', 'cb')` finds a result (the "b").
* `match('^(?<!a)b', 'cb')` fails (we are looking for a "b" at the begining of the text).
  The is equivalent to '^b'.
* `match('^(?<!a)b', 'b')` matches.
* `match('^.(?<!a)b', 'cb')` matches. The text must start with a character other than "a".

> `.(?<!a)b` is not equivalent to `[^a](?<!a)b`. `[^a]` matches `\n` while `.` (by default) does not.

## Positive look-behind

Code [here](code/re_positive_look_behind.py)

Look for "b" preceded by "a":
    
    (?<=a)b

Please note:

* This expression matches **one and exactly one** character: "b".
* An "b" that is not preceded by any character is, even more so, not preceded by a "a".

Thus:

* `match('(?<=a)b', 'b')` Fails. "b" should not be the first character of the text.
* `match('(?<=a)b', 'ab')` Fails. "b" is indeed preceded by "a".
  However, this expression matches **one and exactly one** character: "b".
  When used with "match", it implies that "b" should be the first character in the text...
  which is impossible.
* `search('a(?<=a)b', 'ab')` Matches "ab". We look for _an "a" followed by a "b" preceded itself by an "a"._

# Lazy

    p: Pattern = re.compile('(a+?)')
    m: Optional[Match] = p.match('aaaa')
    print(m.group(0))  # => a
    print(m.group(1))  # => a

# Named groups

    p: Pattern = re.compile('(?P<m1>[a-z]+)(?P<m2>\\d+)')
    m: Optional[Match] = p.match('ab12')
    print(m.group('m1'))  # => ab
    print(m.group('m2'))  # => 12

# Non capturant "()"

    p: Pattern = re.compile('(?:a+)ab')
    m: Optional[Match] = p.match('aaaab')
    print(m.group(0))  # => aaaab
    print(len(m.groups()))  # => 0

# Tips

## Look for a single line that spans on several lines

    p: Pattern = re.compile('^(.+)(?<=a)b')
    m: Optional[Match] = p.search('ab')
    print(m.group(0))  # => ab

...

    m: Optional[Match] = p.search('aaab')
    print(m.group(0))  # => aaab

...

    p: Pattern = re.compile('^(.)(?<=\\\\)\\n')
    m: Optional[Match] = p.search("\\\n")
    pprint(m.group(0))  # => '\\\n'
    print(m.group(1))  # => \

...

    p: Pattern = re.compile('^((.)(?<=\\\\)\\n)')
    m: Optional[Match] = p.search("\\\n")
    pprint(m.group(0))  # => '\\\n'
    pprint(m.group(1))  # => '\\\n'
    pprint(m.group(2))  # => '\\'

...

    p: Pattern = re.compile('^((?:.)(?<=\\\\)\\n)')
    m: Optional[Match] = p.search("\\\n")
    pprint(m.group(0))  # => '\\\n'
    pprint(m.group(1))  # => '\\\n'
    pprint(len(m.groups()))  # => 1
    print('---')

We get it!

    p: Pattern = re.compile('^(((?:.)(?<=\\\\)\\n)|[^\\n])+')
    m: Optional[Match] = p.search("\\\nasc")
    pprint(m.group(0))  # => '\\\nasc'

    text = """abc\\
    def \\
    ghi
    fin
    """
    m: Optional[Match] = p.search(text)
    pprint(m.group(0))  # => 'abc\\\ndef \\\nghi'

## Look for a single BEG ... END

    p: Pattern = re.compile('(.)(?<=E)N')
    m: Match = p.match('EN')
    pprint(m.group(0))  # => EN

...

    p: Pattern = re.compile('(..)(?<=((?<=E)N))D')
    m: Match = p.match('END')
    pprint(m.group(0))  # => END
    pprint(m.group(1))  # => EN

...

    p: Pattern = re.compile('((..)(?<=((?<=E)N))D)')
    m: Match = p.match('END')
    pprint(m.group(0))  # => END

...

    p: Pattern = re.compile('BEGIN [^(?<=((?<=E)N))D]+ END')
    t = "BEGIN aaaa END"
    m: Match = p.match(t)
    pprint(m.group(0))  # => 'BEGIN aaaa END'

...

    t = "BEGIN aaaa END END"
    m: Match = p.match(t)
    pprint(m.group(0))  # => 'BEGIN aaaa END'

...

    p: Pattern = re.compile('BEGIN [^(?<=((?<=E)N))D]+ END', re.MULTILINE)
    t = """BEGIN aaaa
     END
    END
    """
    m: Match = p.match(t)
    pprint(m.group(0))  # => 'BEGIN aaaa\n END'

We get it!

    p: Pattern = re.compile('BEGIN[\n\t ]+[^(?<=((?<=E)N))D]+[\n\t ]+END', re.MULTILINE)
    t = """BEGIN
    aaaa
    END
    END
    """
    m: Match = p.match(t)
    pprint(m.group(0))  # => 'BEGIN\naaaa\nEND'

