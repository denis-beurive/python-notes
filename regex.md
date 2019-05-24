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

## Negative look-ahead

Code [here](code/re_negative_look_ahead.py)

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

Result:

    [1] 0   : 'a'

    [2] 0   : 'a'

    [3] 0   : 'a'
    [3] 1   : 'a'

    [4] 0   : 'ac'

    [5] 0   : 'acxx'
    [5] 1   : 'cxx'

    [6] 0   : 'a--'

    [7] 0   : 'ax-'

## Positive look-ahead

"q" followed by "u".

    p: Pattern = re.compile('q(?:u)')
    m: Optional[Match] = p.match("qu")
    print(m.group(0))  # => qu

As you can see, the character "u" is included into the global match.

The "text" that follows can be a regular expression:

    p: Pattern = re.compile('q(?:\\w@\\w)')
    m: Optional[Match] = p.match("qa@b")
    print(m.group(0))  # => qa@b

    m: Optional[Match] = p.match("qab")
    pprint(m)  # => None

# Negative look-behind

Code [here](code/re_negative_look_behind.py)

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

Result:

    [1] 0   : 'cb'

    [2] no match

    [3] 0   : 'b'

    [4] 0   : 'b'

    [5] 0   : 'b'

    [6] 0   : 'cb'
    [6] 1   : 'c'

    [7] 0   : 'cb'
    [7] 1   : 'c'

    [8] 0   : 'cb'
    [8] 1   : 'c'

    [9] 0   : 'cb'
    [9] 1   : 'c'

    [10] 0   : 'cb'
    [10] 1   : 'c'

    [11] 0   : 'aaaaab'
    [11] 1   : 'aaaaa'

# Positive look-behind

"b" preceded by "a"

    p: Pattern = re.compile('(?<=a)b')
    m: Optional[Match] = p.match('ab')
    pprint(m)  # => None

Yep! You read it. It is not an error ! The text "`ab`" does NOT match "`(?<=a)b`" ! What !!! How is it possible ???

"`(?<=a)b`" matches for one and only one character: a "b" (that is preceded by a "a")

To match "ab" you can use "`a(?<=a)b`" or "`.(?<=a)b`"

    p: Pattern = re.compile('a(?<=a)b', re.VERBOSE)
    m: Optional[Match] = p.match('ab')
    print(m.group(0))  # => ab

    p: Pattern = re.compile('.(?<=a)b', re.VERBOSE)
    m: Optional[Match] = p.match('ab')
    print(m.group(0))  # => ab

    p: Pattern = re.compile('(.)(?<=a)b')
    m: Optional[Match] = p.match('ab')
    print(m.group(0))  # => ab
    print(m.group(1))  # => a

## Lazy

    p: Pattern = re.compile('(a+?)')
    m: Optional[Match] = p.match('aaaa')
    print(m.group(0))  # => a
    print(m.group(1))  # => a

## Named regex

    p: Pattern = re.compile('(?P<m1>[a-z]+)(?P<m2>\\d+)')
    m: Optional[Match] = p.match('ab12')
    print(m.group('m1'))  # => ab
    print(m.group('m2'))  # => 12

## Non capturant "()"

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

...

    p: Pattern = re.compile('BEGIN[\n\t ]+[^(?<=((?<=E)N))D]+[\n\t ]+END', re.MULTILINE)
    t = """BEGIN
    aaaa
    END
    END
    """
    m: Match = p.match(t)
    pprint(m.group(0))  # => 'BEGIN\naaaa\nEND'

