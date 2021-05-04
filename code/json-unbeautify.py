from typing import List
import json
import fileinput

lines: List[str] = []
line: str
for line in fileinput.input():
    line = line.strip()
    if 0 == len(line):
        continue
    lines.append(line)

text = "".join(lines)
print(text)
event = json.loads(text)
print(json.dumps(event, sort_keys=True))

