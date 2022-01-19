#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    word = line.rstrip()
    if word.endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("s") or word.endswith("z"):
        word = word + "es"
        print(word)
    elif word.endswith("y"):
        word2 = word[:len(word) - 1]
        if word2.endswith("a") or word2.endswith("e") or word2.endswith("i") or word2.endswith("o") or word2.endswith("u"):
            word = word + "s"
        else:
            word = word[:len(word) - 1] + "ies"
        print(word)
    elif word.endswith("f"):
        word = word[:len(word) - 1] + "ves"
        print(word)
    elif word.endswith("fe"):
        word = word[:len(word) - 2] + "ves"
        print(word)
    elif word.endswith("o"):
        word = word + "es"
        print(word)
    else:
        word = word + "s"
        print(word)
