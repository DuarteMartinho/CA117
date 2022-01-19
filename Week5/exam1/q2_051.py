#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def checkevil(word):
    wordLower = word.lower()
    #print(word)
    if wordLower.count("e") == 1 and wordLower.count("v") == 1 and wordLower.count("i") == 1 and wordLower.count("l") == 1:
        i = 0
        pos = [0, 0, 0, 0]
        while i < len(wordLower):
            if wordLower[i] == "e":
                pos[0] = i
            elif wordLower[i] == "v":
                pos[1] = i
            elif wordLower[i] == "i":
                pos[2] = i
            elif wordLower[i] == "l":
                pos[3] = i
            i += 1
        #print(pos, word)
        if pos == sorted(pos):
            print(word)


for line in lines:
    line = line.strip()
    checkevil(line)
