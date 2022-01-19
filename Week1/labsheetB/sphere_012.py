#!/usr/bin/env python3

import sys
import math
lines = sys.stdin.readlines()
def main():
    for line in lines:
        numbers = line.strip().split()
        start_r = float(numbers[0])
        inc_r = float(numbers[1])
        end_r = float(numbers[2])

        h1 = 'Radius (m)'
        h4 = '-' * len(h1)
        h2 = 'Area (m^2)'
        h5 = '-' * len(h2)
        h3 = 'Volume (m^3)'
        h6 = '-' * len(h3)
        print(f'{h1:>s} {h2:>15s} {h3:>15s}')
        print(f'{h4:>s} {h5:>15s} {h6:>15s}')

        stop = False
        while not stop:
            if start_r > end_r:
                stop = True
                break
            pi = math.pi
            radiusRaw = round(start_r, 2)
            radiusRnd = str(round(start_r, 1))
            radius = (" " * (len(h1) - len(radiusRnd))) + radiusRnd

            areaRaw = (4 * pi * (radiusRaw ** 2))
            areaRnd = str(round(areaRaw, 2))
            areaSplt = areaRnd.split(".")
            if len(areaSplt[1]) == 1:
                areaRnd += "0"
            area = (" " * (len(h1) - len(areaRnd))) + areaRnd

            volumeRaw = ((4 / 3) * (pi) * (radiusRaw ** 3))
            volumeRnd = str(round(volumeRaw, 2))
            volumeSplt = volumeRnd.split(".")
            if len(volumeSplt[1]) == 1:
                volumeRnd += "0"
            volume = (" " * (len(h1) - len(volumeRnd))) + volumeRnd
            print(f'{radius:>s} {area:>15s} {volume:>15s}')
            start_r += inc_r

if __name__ == '__main__':
    main()
