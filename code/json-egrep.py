# This script can be use to "egrep" file that contains JSON serialized dictionary based on:
#
#     - a field path (ex: "path.to.the.field", for {"path":{"to":{"the":{"field":...}}}}).
#     - a Python regular expression.
#
# If the value of the field matches the regular expression, then the line that represents the JSON
# serialized dictionary is printed to the standard output.
#
# Examples:
#
#       python json-egrep.py --path=eve.json --expr=timestamp:".+"
#       python json-egrep.py --path=eve.json --expr=http.url:"^http://"

from typing import List, Pattern, Match, Any, Tuple, Optional
import json
import argparse
import sys
import re


def get_field_value(in_data: dict,
                    in_field_path: List[str]) -> Tuple[bool, Any]:
    """
    Get the value of a field from a given dictionary.

    The field is defined by its "path". For example:

    ["path", "to", "the", "field"] for data={"path":{"to":{"the":{"field":...}}}})

    :param in_data: the dictionary.
    :param in_field_path: the path to the field.
    :return: the function returns 2 values:
    - the first value indicates whether the field was found or not. The value True indicates that the field was found.
    - if the field was found, then the second value represents the value of the field.
    """
    current: Any = in_data
    for name in in_field_path:
        if not isinstance(current, dict):
            return False, None
        if name not in current:
            return False, None
        current = current[name]
    return True, current


parser = argparse.ArgumentParser(description='Grep JSON')
parser.add_argument('--path',
                    dest='path',
                    type=str,
                    required=True,
                    help='the path to the JSON file to grep')
parser.add_argument('--expr',
                    dest='expr',
                    type=str,
                    required=True,
                    help='the search expression')
parser.add_argument('--verbose',
                    dest='verbose',
                    action='store_true',
                    help='verbosity flag')

args = parser.parse_args()
path: str = args.path
expr: str = args.expr
verbose: bool = args.verbose

try:
    tokens = expr.split(":", 1)
    all_fields: str = tokens[0]
    regexp: str = tokens[1]
except ValueError:
    print("ERROR: invalid value for parameter --expr {} "
          "(format must be: <fields list>:<regular expression>)".format(expr))
    sys.exit(1)

fields: List[str] = all_fields.split(".")
pattern: Pattern = re.compile(regexp)

if verbose:
    print('# Searching for: "{}:<{}>"'.format('.'.join(fields), regexp))

line_number: int = 0
with open(path, 'r') as fd:
    while True:
        line: str = fd.readline()
        if not line:
            break
        line_number += 1
        line = line.strip()
        data: dict = {}
        try:
            data = json.loads(line)
        except json.decoder.JSONDecodeError:
            print("ERROR: invalid line #{} (not JSON): {}".format(line_number, line))
            sys.exit(1)
        if not isinstance(data, dict):
            if verbose:
                print("# WARNING: line #{}: JSON does not represent a dictionary: {}".format(line_number, line))
            continue
        found, value = get_field_value(data, fields)
        if not (found and isinstance(value, str)):
            continue
        if verbose:
            print('# Testing "{}"'.format(value))
        m: Optional[Match] = pattern.search(value)
        if m is not None:
            print("{}".format(line))

