# Regular expression

Find all texts that match a given expression:

    import re
    text = "a abc bcd cde Aaa fff\na1 a2 sss"
    regex = re.compile('a[^ ]*', re.I)
    list_of_matches = regex.findall(text)
    print(','.join(list_of_matches)) # => a,abc,Aaa,a1,a2

Test if a texts matches an expression:

    import re
    text = 'User@Domain.com'
    regex = re.compile('^([a-z]+)@([a-z]+\.[a-z]+)$', re.I)
    m = regex.match(text)
    if m is not None:
        print('"%s" matches!' %text)
        print(m.group(0)) # => User@Domain.com
        print(m.group(1)) # => User
        print(m.group(2)) # => Domain.com

