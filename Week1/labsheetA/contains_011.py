#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for words in lines:
    words = words.rstrip().lower().split()
    substring = words[0]
    string = words[1]
    substringlist = list(substring)
    stringlist = list(string)
    i = 0
    while i < len(substringlist):
        i += 1
        letter = substringlist[i - 1]
        if letter in stringlist:
            substringlist.pop(i - 1)
            stringlist.remove(letter)
            i = 0
    if len(substringlist) == 0:
        print(True)
    else:
        print(False)
