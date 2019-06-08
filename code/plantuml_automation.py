# This script automates the process of PlantUML diagrams.
#
# Configuration: edit the variable SOURCE_TARGET.

import os
from typing import Pattern, Match, Dict
import re
import subprocess


PUML = '/path/to/plantuml.jar'
JAVA = '/path/to/java.exe'

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parts_dir: str = os.path.join(current_dir, 'parts')

SOURCE_TARGET: Dict[str, str] = {
    current_dir: os.path.join(current_dir, 'images'),
    parts_dir: os.path.join(parts_dir, 'images')
}

suffix: Pattern = re.compile('^(.+)\\.puml$', re.IGNORECASE)

for src, dst in SOURCE_TARGET.items():
    print(f"Source: {src}\nDestination: {dst}")
    for file in os.listdir(src):
        m: Match = suffix.match(file)
        if m is None:
            continue
        name: str = m.group(1)
        input_file: str = os.path.join(src, f'{name}.puml')
        print(f"\t{name}")
        subprocess.run([JAVA, '-jar', PUML, '-tpng', '-o', dst, input_file])
    print()
