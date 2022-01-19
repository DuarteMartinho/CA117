#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def main(wordA, wordB):
    posWordA = 0
    letter = ""
    for c in wordA:
        if c in wordB:
            letter = c
            break
        posWordA += 1
    wordb = []
    posWordB = 0
    Found = False
    for c in wordB:
        # print(posWordB, letter, c, letter == c and not Found, Found)
        if letter == c and not Found:
            Found = True
        elif not Found:
            posWordB += 1
        wordb.append(c)
    j = 0
    for c in wordb:
        if posWordB == j:
            print(wordA)
        else:
            print(("." * posWordA) + c + "." * (len(wordA) - 1 - posWordA))
        j += 1

for line in lines:
    line = line.strip()
    wordA, wordB = line.split()
    main(wordA, wordB)
