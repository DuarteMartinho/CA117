#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.rstrip().split()
    i = 0
    while i < len(words):
        words[i] = words[i].capitalize()
        i += 1
    print(" ".join(words))
