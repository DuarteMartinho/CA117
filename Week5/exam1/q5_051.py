#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

laptimes = {}
def bestlaptimes(tokens):
    if len(tokens) > 1:
        name = tokens[0]
    else:
        return
    times = tokens[1:]
    lowestMin = int(times[0].split(':')[0])
    lowestSec = 60
    i = 0
    while i < len(times):
        time = times[i].split(":")
        try:
            minutes = int(time[0])
            seconds = int(time[1])
        except ValueError:
            return
        if minutes < lowestMin:
            lowestMin = minutes
            lowestSec = seconds
        elif minutes == lowestMin:
            lowestMin = minutes
            lowestSec = seconds
        i += 1
    laptimes[name] = (lowestMin, lowestSec)
    return lowestMin

def checkwinner(laptime, lowestMin):
    lowestSec = 60
    for k, v in laptime.items():
        if v[0] <= lowestMin:
            name = k
            lowestMin = v[0]
            lowestSec = v[1]
    if len(str(lowestSec)) == 1:
        lowestSec = "0" + str(lowestSec)
    print(f'{name} : {lowestMin}:{lowestSec}')

for line in lines:
    tokens = line.strip().split(" ")
    lastMin = bestlaptimes(tokens)
checkwinner(laptimes, lastMin)
