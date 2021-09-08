# Datetime

## Timestamps

Sometimes you need to convert timestamps given as strings to objects or integers. And other times you need to perform the reverse operations.

```python
import datetime

date_time_str = '2021-09-01T15:21:00.408899+0000'
d = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
timestamp = d.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f%z').timestamp()
t_to_str = datetime.datetime.fromtimestamp(timestamp, tz=d.tzinfo).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
print(t_to_str)
assert date_time_str == t_to_str
```

Generalization:

```python
from __future__ import annotations  # Python 3.7+
from typing import Optional
import datetime
import math


class AwareDateTime:

    SEC_PRECISION: bool = True
    """Flag that specifies whether the precision of dates should be limited to seconds or not."""
    FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
    """The default format for reading ans writing dates."""

    def __init__(self, dt: Optional[datetime.datetime] = None):
        """
        Create a new AwareDateTime object.

        :param dt: an option datetime instance. If not provided, then the constructor will
                   create a date that represents "now".
        """
        if dt is None:
            self.dt: datetime.datetime = AwareDateTime.now()
        else:
            if not AwareDateTime.is_aware(dt):
                raise Exception("The given datetime is not aware!")
            self.dt: datetime.datetime = AwareDateTime._apply_precision(dt)

    def tz_name(self) -> str:
        """
        Return the name of the data timezone.

        :return: the name of the data timezone.
        """
        return "{}".format(self.dt.tzname())

    def tz_offset(self) -> int:
        """
        Return the number of seconds between the date timezone and UTC.

        :return: the number of seconds between the date timezone and UTC.
        """

        return self.dt.utcoffset().seconds

    def unix_timestamp(self) -> int:
        """
        Return a UNIX timestamp that represents the date.

        :return: a UNIX timestamp that represents the date.
        """
        return math.floor(self.dt.timestamp())

    def to_str_timestamp(self) -> str:
        """
        Return a textual timestamp that represents the date.

        :return: a textual timestamp that represents the date.
        """
        return self.dt.strftime(AwareDateTime.FORMAT)

    def __str__(self) -> str:
        return self.to_str_timestamp()

    def __repr__(self) -> str:
        return self.to_str_timestamp()

    def __eq__(self, other: AwareDateTime) -> bool:
        if self.tz_offset() != other.tz_offset():
            return False
        if self.dt.timetuple() != other.dt.timetuple():
            return False
        return True

    @staticmethod
    def is_aware(dt: datetime.datetime) -> bool:
        """
        Test whether a given datetime object is aware or not.

        A datetime object d is aware if both of the following hold:
          -  d.tzinfo is not None
          -  d.tzinfo.utcoffset(d) does not return None

        See https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive

        :param dt: the datetime object to test.
        :return: True if the given datetime object is aware. False otherwise.
        """
        return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None

    @staticmethod
    def now() -> datetime.datetime:
        """
        Return a datetime object that represents "now".

        :return: a datetime object that represents "now".
        """
        now = datetime.datetime.now(tz=datetime.timezone.utc).astimezone()
        if not AwareDateTime.SEC_PRECISION:
            return now
        return AwareDateTime._apply_precision(now)

    @staticmethod
    def sys_tz_name() -> str:
        """
        Return the name of the current system timezone.

        :return: the name of the current system timezone.
        """
        return "{}".format(AwareDateTime.now().tzname())

    @staticmethod
    def sys_tz_offset() -> int:
        """
        Return the number of seconds between the current system timezone and UTC.

        :return: the number of seconds between the current system timezone and UTC.
        """
        return AwareDateTime.now().utcoffset().seconds

    @staticmethod
    def from_unix_timestamp(unix_timestamp: int, tz: Optional[datetime.tzinfo] = None) -> AwareDateTime:
        """
        Create a AwareDateTime object from a given UNIX timestamp.

        :param unix_timestamp: the UNIX timestamp.
        :param tz: a, optional timezone. If not specified, then use the current system timezone.
        :return: a new AwareDateTime object.
        """
        if tz is None:
            tz = AwareDateTime.now().tzinfo
        return AwareDateTime(datetime.datetime.fromtimestamp(unix_timestamp, tz))

    @staticmethod
    def from_str_timestamp(timestamp: str) -> AwareDateTime:
        """
        Create a AwareDateTime object from a given textual timestamp.

        :param timestamp: the textual timestamp. This timestamp must match the given default date format.
        :return: a new AwareDateTime object.
        """
        dt = datetime.datetime.strptime(timestamp, AwareDateTime.FORMAT)
        return AwareDateTime(dt)

    @staticmethod
    def _apply_precision(dt: datetime.datetime) -> datetime.datetime:
        if not AwareDateTime.SEC_PRECISION:
            return dt
        unix_timestamp = math.floor(dt.timestamp())
        return datetime.datetime.fromtimestamp(unix_timestamp, dt.tzinfo)


def test_general():

    # Test equality operator
    delta = datetime.timedelta(seconds=1)
    now = AwareDateTime()
    other_data = AwareDateTime(now.dt + delta)
    assert now != other_data
    other_data = AwareDateTime(other_data.dt - delta)
    assert now == other_data


def test_sec_precision_activated():

    # Test the creation of an AwareDateTime instance from a unix timestamp.
    now = AwareDateTime()
    now_clone = AwareDateTime.from_unix_timestamp(now.unix_timestamp())
    assert now == now_clone
    print("{}: {}".format(now.dt, now.unix_timestamp()))
    print("{}: {}".format(now_clone.dt, now_clone.unix_timestamp()))

    # Test the creation of an AwareDateTime instance from a textual timestamp.
    tt_str = now_clone.to_str_timestamp()
    new_clone = AwareDateTime.from_str_timestamp(tt_str)
    assert new_clone == now
    print("{}".format(tt_str))
    print("{}".format(new_clone.to_str_timestamp()))


def test():
    test_general()
    test_sec_precision_activated()


test()
```
