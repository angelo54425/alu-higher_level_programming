#!/usr/bin/python3
def fizzbuzz():
    for x in range(101):
        if x % 3 == 0 and x%5 == 0:
            print(x, '')
        elif x % 3:
            print(x, '')
        elif x % 5:
            print(x, '')
        else:
            print(x, '')
