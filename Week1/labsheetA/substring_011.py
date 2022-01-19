#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for words in lines:
    words = words.rstrip().split()
    string = words[1].lower()
    substring = words[0].lower()

    if substring in string:
        print(True)
    else:
        print(False)
