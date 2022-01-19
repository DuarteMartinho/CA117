#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
litresAvailable = int(lines[0].strip())
buckets = lines[1].strip().split()
i = 0
for bucket in buckets:
    bucket = int(bucket)
    if litresAvailable - bucket >= 0:
        litresAvailable -= bucket
        i += 1
    else:
        break
print(i)
