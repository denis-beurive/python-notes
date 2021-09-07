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

