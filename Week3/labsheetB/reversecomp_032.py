#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

def binarySearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False

wordsList = [line.strip() for line in words]
sortedWords = sorted([w.lower() for w in wordsList])

revs = [w for w in wordsList if len(w) >= 5 and binarySearch(w[::-1].lower(), sortedWords)]
print(revs)
