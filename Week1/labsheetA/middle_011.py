#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for word in lines:
    word = word.rstrip()
    chars = len(word)
    if chars % 2 == 0:
        print("No middle character!")
    else:
        chars = chars // 2
        print(word[chars])
