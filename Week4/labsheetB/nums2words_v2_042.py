#!/usr/bin/env python3

import sys
availableNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
numsEng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
lines = sys.stdin.readlines()

def main(line):
    i = 0
    while i < len(line):
        num = line[i]
        if num in availableNums:
            line[i] = num.replace(num, numsEng[int(num)], 1)
        else:
            line[i] = num.replace(num, "unknown", 1)
        i += 1
    print(" ".join(line))

for line in lines:
    line = line.strip().split()
    main(line)
