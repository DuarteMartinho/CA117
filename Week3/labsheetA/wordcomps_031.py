#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
def anagram(left, right):
    for c in left:
        if c in right:
            right = right.replace(c, "", 1)
        else:
            return False
    return right == ""
def main(allwords):
    words18 = [word.strip() for word in words if len(word.strip()) > 17]
    words17 = [word.strip() for word in words if len(word.strip()) == 17]
    words4a = [word.strip() for word in words if word.strip().lower().count("a") == 4]
    words2q = [word.strip() for word in words if word.strip().lower().count("q") >= 2]
    wordscie = [word.strip() for word in words if "cie" in word.strip()]
    wordsanagrams = [word.strip() for word in words if anagram(word.strip().lower(), "angle") and len(word.strip().lower()) == 5 and word.strip().lower() != "angle"]
    print("Words containing 17 letters: " + str(words17))
    print("Words containing 18+ letters: " + str(words18))
    print("Words with 4 a's: " + str(words4a))
    print("Words with 2+ q's: " + str(words2q))
    print("Words containing cie: " + str(wordscie))
    print("Anagrams of angle: " + str(wordsanagrams))
main(words)
