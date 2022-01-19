#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

d_define = {}
numsInDict = []
operators = ["+", "-", "="]

# IN : word to checked it is in the dictionary
# OUT : returns unknown or value for word
def lookup(word):
    if word in d_define:
        return d_define[word]
    else:
        return "unknown"

# IN : answer to check if there is a word assigned to it a dictionary
# OUT : returns unknown or word assigned to answer
def getAnswer(answer):
    for k, v in d_define.items():
        if v == answer:
            return k
    return "unknown"

# IN : All values to calc (includes operators)
# OUT : print unknown or word if in dict
def calc(args):
    equation = 0
    lastOperator = "+"
    for word in args:
        if word not in operators:
            res = lookup(word)
            if res == "unknown":
                return "unknown"
            else:
                #print(res)
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

# IN : word to be added and its value
# OUT : updated dictionary
def define(word, num):
    num = int(num)
    if num in numsInDict or word in d_define:
        # print(f'NEEDS REPLACE')
        # print(f'same value -> {num in numsInDict}')
        # print(f'same word -> {word in d_define}')
        # print(f'same word -> {d_define}')
        # print(f'same word -> {numsInDict}')
        topop = ""
        for k, v in d_define.items():
            if k == word:
                d_define[word] = num  # Update Word with new value
            elif v == num:
                topop = k  # Saves value to pop later
        if topop != "":
            d_define.pop(topop)
            d_define[word] = num
    else:
        d_define[word] = num
        numsInDict.append(num)
    #print(f'{word} - {d_define[word]}')

for line in lines:
    #print(f'-------------------------------------- LOOP START ------------------------------------')
    line = line.rstrip().split()
    #print(f'Line Split - {line}')
    if len(line) == 3 and line[0] == "def":
        define(line[1], line[2])
    elif len(line) > 1 and line[len(line) - 1] == "=":
        result = calc(line[1:])
        print(f'{" ".join(line[1:]) + " " + result}')
    elif len(line) == 1 and line[0] == "clear":
        d_define = {}
        wordsInDict = []
        numsInDict = []
        #print(f'Cleared d_define - {d_define} {wordsInDict}')
    #print(d_define)
    #print(f'--------------------------------------- LOOP END -------------------------------------')
