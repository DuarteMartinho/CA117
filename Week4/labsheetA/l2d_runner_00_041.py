#!/usr/bin/env python3

import sys

from l2d_041 import l2d

def main():
    d = l2d(sys.stdin.readlines())
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))
              
if __name__ == '__main__':
    main()