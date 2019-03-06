# CLI parsing with argparse

## Warning

There is only one way to add an "entity" (whether it is an "_argument_" or an "_option_") to the description of the command line: the method `add_argument()`.

This method applies for declaring both arguments and options... which is confusing. Indeed, we expect to have two methods :

* One method declare an argument (`add_argument()` is fine).
* One method declare an option (`add_option()` would be fine).

Other than the name of the single method that applies for both arguments and options, the signature of this method is also confusing. Some combinations of options make sense in the context of an argument, but not in the context of an option, and reciprocally.

Providing two functions would not totally eliminate the ambiguity. However it would probably narrow it.

## Example 1

    import argparse
    from pprint import pprint

    cli = '2 4 4'
    print(f'### Test: {cli}')
    parser = argparse.ArgumentParser(description='Test 1')
    parser.add_argument('integers',
                        action='store',  # This is the default action:
                                         # just store the value of the argument in the "namespace".
                        nargs='+',       # The number of command-line arguments that should be consumed.
                                         # +: at least onr argument.
                        type=int,        # The type of the argument.
                        metavar='N',     # A name for the argument in usage messages.
                        choices=[2,4,6], # A container of the allowable values for the argument.
                        help='an integer')
    args = parser.parse_args(cli.split())
    pprint(args.integers) # => [2, 4, 4]

## Example 2

    import argparse
    from pprint import pprint

    cli = '2 s1 s2'
    print(f'### Test: {cli}')
    parser = argparse.ArgumentParser(description='Test 2')
    parser.add_argument('integer',
                        action='store',
                        nargs=1,
                        type=int,
                        help='an integer')
    parser.add_argument('strings',
                        action='store',
                        nargs='*',       # *: any number of arguments.
                        type=str,
                        help='an integer')
    args = parser.parse_args(cli.split())
    pprint(args.integer) # => [2]
    pprint(args.strings) # => ['s1', 's2']

## Example 3

    import argparse
    from pprint import pprint

    cli = '2 s1 s2'
    print(f'### Test: {cli}')
    parser = argparse.ArgumentParser(description='Test 2')
    parser.add_argument('integer',
                        action='store',
                        nargs=1,
                        type=int,
                        help='an integer')
    parser.add_argument('strings',
                        action='store',
                        nargs='*',
                        type=str,
                        help='0 or more strings')
    parser.add_argument('--verbose',
                        dest='verbose-flag',
                        action='store_true',
                        help='an integer')

    args = parser.parse_args(cli.split())
    pprint(args.integer) # => [2]
    pprint(args.strings) # => ['s1', 's2']
    pprint(args.__getattribute__('verbose-flag')) # => False

## Example 4

    import argparse
    from pprint import pprint

    # Note that both command lines below are valid:
    #    * 2 s1 s2 --verbose --path /tmp/toto
    #    * 2 s1 s2 --verbose --path=/tmp/toto

    cli = '2 s1 s2 --verbose --path /tmp/toto'
    print(f'### Test: {cli}')
    parser = argparse.ArgumentParser(description='Test 2')
    parser.add_argument('integer',
                        action='store',
                        nargs=1,
                        type=int,
                        help='an integer')
    parser.add_argument('strings',
                        action='store',
                        nargs='*',
                        type=str,
                        help='0 or more strings')
    parser.add_argument('--verbose',
                        dest='verbose-flag',
                        action='store_true',
                        help='verbosity flag')
    parser.add_argument('--path',
                        dest='path',
                        type=str,
                        required=True,
                        help='the path')

    args = parser.parse_args(cli.split())
    pprint(args.integer) # => [2]
    pprint(args.strings) # => ['s1', 's2']
    pprint(args.__getattribute__('verbose-flag')) # => True
    pprint(args.path) # => '/tmp/toto'

## Example 5

    import argparse
    from pprint import pprint

    # Note that all the command lines below are valid:
    #    * 2 s1 s2 --path /tmp/toto /tmp/titi --verbose
    #    * --path /tmp/toto /tmp/titi --verbose 2 s1 s2
    #    * --path /tmp/toto /tmp/titi --verbose -- 2 s1 s2
    #    * --path /tmp/toto /tmp/titi --verbose -- 2 s1 --s2

    cli = '--path /tmp/toto /tmp/titi --verbose 2 s1 s2'
    print(f'### Test 2: {cli}')
    parser = argparse.ArgumentParser(description='Test 2')
    parser.add_argument('integer',
                        action='store',
                        nargs=1,
                        type=int,
                        help='an integer')
    parser.add_argument('strings',
                        action='store',
                        nargs='*',
                        type=str,
                        help='0 or more strings')
    parser.add_argument('--verbose',
                        dest='verbose-flag',
                        action='store_true',
                        help='verbosity flag')
    parser.add_argument('--path',
                        dest='path',
                        type=str,
                        nargs='+',
                        required=True,
                        help='the path')

    args = parser.parse_args(cli.split())
    pprint(args.integer) # => [2]
    pprint(args.strings) # => ['s1', 's2']
    pprint(args.__getattribute__('verbose-flag')) # => True
    pprint(args.path) # => ['/tmp/toto', '/tmp/titi']
    print('')

    args = parser.parse_args('--path /tmp/toto /tmp/titi --verbose -- 2 s1 --s2'.split())
    pprint(args.integer) # => [2]
    pprint(args.strings) # => ['s1', '--s2']
    pprint(args.__getattribute__('verbose-flag')) # => True
    pprint(args.path) # => ['/tmp/toto', '/tmp/titi']

## Example 6: different options (not arguments!) can end up to the same destination

    import argparse
    from pprint import pprint

    cli = '--int i1 --str s1 s2 --any'
    print(f'### Test: {cli}')
    parser = argparse.ArgumentParser(description='Test 2')
    parser.add_argument('--str',
                        dest='type',
                        type=str,
                        nargs='+',
                        action='append',
                        help='first type')
    parser.add_argument('--int',
                        dest='type',
                        action='append',
                        help='second type')
    parser.add_argument('--any',
                        dest='type',
                        action='append_const',
                        const=True,
                        help='second type')

    args = parser.parse_args(cli.split())
    pprint(args.type) # => ['i1', ['s1', 's2'], True]


