#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -=1
    print ("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

def fizzbuzzPrinter():
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz(num=None):
    if num is None:
       
        for i in range(1, 101):
            print(fizzbuzz(i))
        return
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

