#!/usr/bin/env python3
import re
import sys

if len(sys.argv) != 2:
    print("Usage\n\tyamlize.py FILE\n", file=sys.stderr)
    exit(1)

fname = sys.argv[1]

tit_pattern = re.compile(r"^Titulo .+$")
cap_pattern = re.compile(r"^Capitulo .+$")
art_pattern = re.compile(r"^Articulo \d+.+$")

output_file = "result.yaml"
with open(fname) as in_f, open(output_file, "w") as out_f:
    for line in in_f:
        line = line.strip()
        if tit_pattern.match(line):
            out_f.write(f"- {line}:\n")
        elif cap_pattern.match(line):
            out_f.write(f"- {line}:\n")
        elif art_pattern.match(line):
            art, text = line.split(".", maxsplit=1)
            out_f.write(f"  - {art.strip()}: |\n      {text.strip()}\n")
        elif line:
            out_f.write(f"      {line}\n")
