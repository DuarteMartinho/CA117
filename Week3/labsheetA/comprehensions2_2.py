#!/usr/bin/env python3

s = "Are vowels required to understand sentences?"
extract_nonVowels = [c for c in s if c.lower() not in "aeiou"]
print("".join(extract_nonVowels))