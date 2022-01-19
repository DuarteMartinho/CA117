#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

longest = 0

for line in lines:
    line = line.rstrip()
    if len(line) > longest:
        longest = len(line)

for line in lines:
    line = line.rstrip()
    lenLine = len(line)
    totalSpace = longest - lenLine
    space = (totalSpace) // 2
    space2 = totalSpace - space
    newLine = (space * " ") + line + (space2 * " ")
    print(newLine)
