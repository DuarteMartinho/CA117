#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
d_define = {}
numsInDict = []
operators = ["+", "-", "="]
def lookup(word):
    if word in d_define:
        return d_define[word]
    else:
        return "unknown"
def getAnswer(answer):
    for k, v in d_define.items():
        if v == answer:
            return k
    return "unknown"
def calc(args):
    equation = 0
    lastOperator = "+"
    for word in args:
        if word not in operators:
            res = lookup(word)
            if res == "unknown":
                return "unknown"
            else:
                if lastOperator == "+":
                    equation += res
                else:
                    equation -= res
        else:
            lastOperator = word
    if equation in numsInDict:
        res = getAnswer(equation)
        return res
    else:
        return "unknown"
def define(word, num):
    num = int(num)
    if num in numsInDict or word in d_define:
        topop = ""
        for k, v in d_define.items():
            if k == word:
                d_define[word] = num
            elif v == num:
                topop = k
        if topop != "":
            d_define.pop(topop)
            d_define[word] = num
    else:
        d_define[word] = num
        numsInDict.append(num)
for line in lines:
    line = line.rstrip().split()
    if len(line) == 3 and line[0] == "def":
        define(line[1], line[2])
    elif len(line) > 1 and line[len(line) - 1] == "=":
        result = calc(line[1:])
        print(f'{" ".join(line[1:]) + " " + result}')
    elif line[0] == "clear":
        d_define = {}
        wordsInDict = []
