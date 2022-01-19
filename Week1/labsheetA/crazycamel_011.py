#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.rstrip().split()
    i = 0
    while i < len(words):
        line = words[i][::-1]
        letters = line.capitalize()
        words[i] = letters[::-1]
        i += 1
    print(" ".join(words))
