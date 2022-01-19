#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.rstrip().split(" ")
    i = 0
    found = False
    while i < len(words) and not found:
        word = words[i]
        if word[0] == "m":
            words[i] = word.capitalize()
            found = True
        i += 1
    print(" ".join(words))
