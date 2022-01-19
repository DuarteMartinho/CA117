#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def checkLongest(word):
    pos = [0, 0]
    i = 0
    start = 0
    end = 0
    UpperStart = True
    while i < len(word):
        #print(i, word[i], word[i].isupper(), start == 0 and word[i].isupper())
        if UpperStart and word[i].isupper():
            start = i

        if word[i].isupper():
            UpperStart = False
            end = i + 1
            diff = pos[1] - pos[0]
            if end - start > diff and i + 1 >= len(word):
                pos[0] = start
                pos[1] = end
        else:
            UpperStart = True
            diff = pos[1] - pos[0]
            if end - start > diff:
                pos[0] = start
                pos[1] = end
        #print(word[i], word[i].isupper(), UpperStart, start, end)
        #print(f'Diff - {pos} --> {word}')
        i += 1
    print(word[pos[0]:pos[1]])

for line in lines:
    line = line.strip()
    checkLongest(line)
