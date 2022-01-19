#!/usr/bin/env python3

def extract_nonVowels(s):
    nonVowels = []
    for c in s:
        if c.lower() not in "aeiou":
            nonVowels.append(c)
    s = "".join(nonVowels)
    return s

s = "Are vowels required to understand sentences?"
print(extract_nonVowels(s))