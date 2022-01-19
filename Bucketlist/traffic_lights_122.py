#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def waitTime(eliza, red, green):
    time = 0
    isRed = True
    while time <= eliza:
        if isRed:
            time = time + red
            isRed = False
        elif not isRed:
            time = time + green
            isRed = True
    if not isRed:
        wait = time - eliza
    elif isRed:
        wait = 0
    return wait

km = int(lines[0].strip())
trafficlights = lines[1:]

time = 0
currentKm = 0
for tl in trafficlights:
    d, r, g = tl.strip().split()
    # print(f'{d}, {r}, {g}')
    time += (int(d) - currentKm)
    currentKm = int(d)
    wait_time = waitTime(time, int(r), int(g))
    time += wait_time
    # print(time)

# When done needs to add remaining KM after last traffic light
time += (km - currentKm)
print(time)
