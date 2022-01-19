#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
vowels = "aeiou"

def main(allwords):
    SmallestWordWithVowels = ""
    WordsendingInIary = 0
    WordsWithMostsE = []
    TotalWordsWithE = 0
    for word in words:
        wordNotLower = word.strip()
        word = word.strip().lower()
        HasAllVowels = False
        if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word:
            HasAllVowels = True

        if HasAllVowels:
            if SmallestWordWithVowels == "":
                SmallestWordWithVowels = wordNotLower
            elif len(SmallestWordWithVowels) > len(word):
                SmallestWordWithVowels = wordNotLower
        lenWord = len(word)
        if lenWord > 4 and word[lenWord - 4:] == "iary":
            WordsendingInIary += 1

        if word.count("e") > TotalWordsWithE:
            WordsWithMostsE = []
            WordsWithMostsE.append(wordNotLower)
            TotalWordsWithE = word.count("e")
        elif word.count("e") == TotalWordsWithE:
            WordsWithMostsE.append(wordNotLower)
            TotalWordsWithE = word.count("e")

    print("Shortest word containing all vowels: " + SmallestWordWithVowels)
    print("Words ending in iary: " + str(WordsendingInIary))
    print("Words with most e's: " + str(WordsWithMostsE))

main(words)
