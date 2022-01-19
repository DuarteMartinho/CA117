#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    words = line.rstrip().split(".")
    secondName = words[1].split("@")
    firstName = words[0]
    secondName = secondName[0]
    i = 0
    while i < len(secondName) and (secondName[i] <= "0" or "9" <= secondName[i]):
        i += 1
    firstName = firstName.capitalize()
    secondName = secondName[:i].capitalize()
    lineout = firstName + " " + secondName
    print(lineout)
