#!/usr/bin/env python3

import sys
from string import punctuation
lines = sys.stdin.read()

def main(lines):
    allWords = {}
    allWords["a"] = lines.count("a")
    allWords["e"] = lines.count("e")
    allWords["i"] = lines.count("i")
    allWords["o"] = lines.count("o")
    allWords["u"] = lines.count("u")
    return allWords

def tagger(item):
   return item[1]

dictionaryOrdered = {}
def output(dictionary):
    longest = 0
    for k, v in sorted(dictionary.items(), key=tagger, reverse=True):
        if len(str(v)) > longest:
            longest = len(str(v))
        dictionaryOrdered[k] = v

    for k, v in dictionaryOrdered.items():
        print(f'{k} : {(longest - len(str(v))) * " "}{v}')
allWords = main(lines.strip().lower())
output(allWords)
