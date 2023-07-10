#!/usr/bin/python3
def fizzbuzz():
    for x in range(101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz" + " ")
        elif x % 3:
            print("Fizz" + " ")
        elif x % 5:
            print("Buzz" + " ")
        else:
            print("{}".format(x) + " ")
