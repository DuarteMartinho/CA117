#!/usr/bin/env python3

import sys
filename = sys.argv[1]
lines = sys.stdin.readlines()
calories = {}
calculatedCalories = {}

with open(filename, "r") as f:
    output = f.readlines()
    for line in output:
        line = line.strip()
        i = 0
        for c in line:
            if c.isdigit():
                break
            i += 1
        ingridient = line[:i - 1]
        value = line[i:]
        calories[ingridient] = int(value)

def calculateCalories(name, ingredients):
    calculatedCalories[name] = 0
    for ingredient in ingredients:
        if ingredient in calories:
            calculatedCalories[name] += calories[ingredient]
        else:
            calculatedCalories[name] += 100

def printOut(longestName):
    # print(calculatedCalories, longestName)
    longestValue = 0
    for k, v in calculatedCalories.items():
        if len(str(v)) > longestValue:
            longestValue = len(str(v))

    for k, v in sorted(calculatedCalories.items(), key=lambda item: item[1]):
        print(f'{(longestName - len(k)) * " "}{k} : {(longestValue - len(str(v))) * " "}{v}')

longestName = 0
for line in lines:
    tokens = line.strip().split(',')
    name = tokens[0]
    if len(name) > longestName:
        longestName = len(name)
    calculateCalories(name, tokens[1:])

printOut(longestName)
