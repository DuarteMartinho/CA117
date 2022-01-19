#!/usr/bin/env python3

import sys
import calendar
lines = sys.stdin.readlines()
poem = ["Monday and Monday's child is fair of face.", "Tuesday and Tuesday's child is full of grace.", "Wednesday and Wednesday's child is full of woe.", "Thursday and Thursday's child has far to go.", "Friday and Friday's child is loving and giving.", "Saturday and Saturday's child works hard for a living.", "Sunday and Sunday's child is fair and wise and good in every way."]
def weekday(year, month, day):
    weekday = poem[calendar.weekday(year, month, day)]
    return weekday

for line in lines:
    line = line.rstrip().split()
    day, month, year = line
    print(f'You were born on a {weekday(int(year), int(month), int(day))}')
