#!/usr/bin/env python3

import sys
availableNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
numsEng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
filename = sys.argv[1]
lines = sys.stdin.readlines()

def main(line, translation):
    i = 0
    while i < len(line):
        num = line[i]
        if num in availableNums:
            wordEng = numsEng[int(num)]
            output = translation[wordEng]
            line[i] = num.replace(num, output, 1)
        else:
            line[i] = num.replace(num, "unknown", 1)
        i += 1
    print(" ".join(line))

d = {}
with open(filename, "r") as f_in:
    for line in f_in:
        english, german = line.strip().split()
        d[english] = german

for line in lines:
    line = line.strip().split()
    main(line, d)
