# Compare 2 timestamps.
#
# WARNING: the format of the timestamps must be "%Y-%m-%dT%H:%M:%S.%f%z".
#
# Example:
#
#     python timestamp_compare.py '2021-10-22T08:03:00.000000+0000' '2021-10-22T10:03:00.000000+0200'

import datetime
import argparse

parser = argparse.ArgumentParser(description='Compare 2 timestamps (format "%Y-%m-%dT%H:%M:%S.%f%z")')
parser.add_argument('timestamp1',
                    action='store',
                    nargs=1,
                    type=str,
                    help='first timestamp (format "%Y-%m-%dT%H:%M:%S.%f%z")')
parser.add_argument('timestamp2',
                    action='store',
                    nargs=1,
                    type=str,
                    help='second timestamp (format "%Y-%m-%dT%H:%M:%S.%f%z")')
args = parser.parse_args()
str_timestamp1: str = args.timestamp1[0]
str_timestamp2: str = args.timestamp2[0]

local_timezone: datetime.tzinfo = datetime.datetime.utcnow().astimezone().tzinfo
format: str = '%Y-%m-%dT%H:%M:%S.%f%z'
date_timestamp1: datetime.datetime = datetime.datetime.strptime(str_timestamp1, format)
date_timestamp2: datetime.datetime = datetime.datetime.strptime(str_timestamp2, format)
int_timestamp1: float = date_timestamp1.timestamp()
int_timestamp2: float = date_timestamp2.timestamp()

print("timestamp1: {} -> {}".format(date_timestamp1, int_timestamp1))
print("timestamp2: {} -> {}".format(date_timestamp2, int_timestamp2))
