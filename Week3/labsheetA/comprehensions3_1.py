#!/usr/bin/env python3

def main(listIn):
    newList = []
    for i in listIn:
        if i % 2 == 0:
            i = i ** 2
            newList.append(i)
    return newList

intergers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
res = main(intergers)
print(res)