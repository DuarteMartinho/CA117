#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

def main(words):
    newList = []
    for word in words:
        low = word.rstrip().lower()
        if low[-1] == "q":
            newList.append(word.rstrip())
        else:
            i = 0
            while i < (len(low) - 1):
                if low[i] == "q" and low[i + 1] != "u":
                    newList.append(word.rstrip())
                i += 1
    return newList

res = main(words)
print("Words with q but no u: " + str(res))
