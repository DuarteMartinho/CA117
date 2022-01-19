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
        try:
            mark = int(tokens[0])
        except ValueError:
            print(f'Invalid mark {tokens[0]} encountered. Skipping.')

        if mark > highest:
            names = []
            highest = mark
            name = " ".join(tokens[1:])
            names.append(name)
        elif mark == highest:
            name2 = " ".join(tokens[1:])
            names.append(name2)
        i += 1
    # print(highest, pos)
    # print(name)
    namesLine = ", ".join(names)
    print(f'Best student(s): {namesLine}\nBest mark: {highest}')
except FileNotFoundError:
    print(f'The file {filename} could not be opened.')
