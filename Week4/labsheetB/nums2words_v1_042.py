#!/usr/bin/env python3

import sys
numsEng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
lines = sys.stdin.readlines()

def main(line):
    i = 0
    while i < len(line):
        num = line[i]
        line[i] = num.replace(num, numsEng[int(num)], 1)
        i += 1
    print(" ".join(line))

for line in lines:
    line = line.strip().split()
    main(line)
