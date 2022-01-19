#!/usr/bin/env python3

import sys
from string import punctuation
lines = sys.stdin.readlines()

allWords = {}
def main(line):
    for word in line:
        rev_word = word[::-1]
        for c in rev_word:
            if c in punctuation:
                rev_word = rev_word.replace(c, "", 1)
            else:
                break
        word = rev_word[::-1]
        if word not in allWords:
            allWords[word] = 1
        else:
            allWords[word] += 1

def output(dictionary):
    for k, v in dictionary:
        print('{} : {}'.format(k, v))

for line in lines:
    line = line.strip().lower().split()
    main(line)

output(sorted(allWords.items()))
