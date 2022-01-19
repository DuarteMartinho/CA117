#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for word in lines:
    word = word.rstrip()
    middle = word.rstrip()[1:-1]
    if len(word) > 1:
        first = word[0].capitalize()
        last = word[len(word) - 1].capitalize()
        print(first + middle + last)
