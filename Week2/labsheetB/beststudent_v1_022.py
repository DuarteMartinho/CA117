#!/usr/bin/env python3

import sys
filename = sys.argv[1]

try:
    with open(filename, "r") as f_in:
        lines = f_in.readlines()
    # print(lines)
    highest = 0
    i = 0
    while i < len(lines):
        tokens = lines[i].rstrip().split()
        mark = int(tokens[0])
        if mark > highest:
            highest = mark
            name = " ".join(tokens[1:])
        i += 1
    # print(highest, pos)
    # print(name)
    print(f'Best student: {name}\nBest mark: {highest}')

except FileNotFoundError:
    print(f'The file {filename} could not be opened.')
