#!/usr/bin/env python3

def extract_odds(num):
    odds = []
    for n in num:
        if n % 2:
            odds.append(n)
    return odds

lon = [3, 4, 5, 1, 6, 7]
loo = extract_odds(lon)
print(loo)