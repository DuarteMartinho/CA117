#!/usr/bin/env python3

import sys
namesIn = sys.stdin.readlines()
FileName = sys.argv[1]
contact = {}
with open(FileName, "r") as f_in:
    lines = f_in.readlines()
    for line in lines:
        name, number = line.strip().split()
        contact[name] = number

for name in namesIn:
    try:
        print(f'Name: {name.strip()}')
        print(f'Phone: {contact[name.strip()]}')
    except KeyError:
        print(f'No such contact')
