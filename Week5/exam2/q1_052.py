#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def rotate(line):
    s, n = line.split()
    i = 0
    while i < int(n):
        rotateLetter = s[len(s) - 1]
        slice_s = s[:len(s) - 1]
        s = rotateLetter + slice_s
        i += 1
    return s

for line in lines:
    line = line.strip()
    res = rotate(line)
    print(res)
