#!/usr/bin/env python3

dictionary = {}
def l2d(allwords):
    line1, line2 = allwords
    line1 = line1.strip().split()
    line2 = line2.strip().split()
    i = 0
    while i < len(line1):
        animal = line1[i]
        number = line2[i]
        dictionary[animal] = number
        i += 1
    return dictionary
