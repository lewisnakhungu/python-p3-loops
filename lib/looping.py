#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0 :
        print (counter)
        counter -= 1
    print ("Happy New Year!")

def square_integers(int_list):
    # code goes here!
   # return [x * x for x in int_list]

   result = []
   for x in int_list:
       result.append(x * x)
   return result

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print( "FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num) 
