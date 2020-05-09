# encoding: utf-8

# importing Modules
import sys
import math
import random
import threading
import time
from functools import reduce

# Print
print("Hello World")  # print cmd
name = input("What's your name: ")  # Input stored in a String Variable
print("Hi ", name)  # print name var

# Data Types
'''All datatypes in python are objects'''
fl = 0.5  # float
integer = 2  # int
iota = 6 + 4j  # complex num : real + imaginary
string = "String"  # str
lst = [23, 41, 567, "Harshit"]  # list
tup = (23, 41, 567, "Harshit")  # tuple
boolean = True  # bool

'''difference between tuples and list'''
lst[0] = 1000
try:
    tup[2] = 1000
except:
    print("SHOWS error because item assignment after initialisation is illegal")

dictionary = {"Ice-creams":
                  [{"company": "Quality Walls",
                    "flavour": "Vanilla (Plain)",
                    "price": 23},
                   {"company": "Premiums",
                    "flavour": "Chocolate",
                    "price": 33}
                   ]
              }  # dictionary with list of dictionaries or JSON format

# Fundamental Operations

print("8 + 2 = ", 8 + 2)  # ADD
print("8 - 2 = ", 8 - 2)  # SUB
print("8 * 2 = ", 8 * 2)  # MUL
print("8 / 2 = ", 8 / 2)  # DIV
print("8 % 2 = ", 8 % 2)  # MODULUS: Remainder
print("8 ** 2 = ", 8 ** 2)  # POWER
print("8 // 2 = ", 8 // 2)  # INTEGER DIVISION : Disregard Remainder

# Math Module : imported math
print("sin(90\u00B0) :", math.sin(math.radians(90)))  # sine
'''
    And many other trigonometric and statistical functions
'''

# Using the random class
print("Random ", random.randint(1, 100))

# Conditions

'''
Comparision Operators
 < > <= >= == !=(not equal)
 
Logical Operators
 and or not
 
Bitwise Operators
 & And
 | Or
 ~ Not
 ^ Xor
 >> right shift
 << left shift
 
Assignment operators
 = += -= *= /= %= //= **=
 &= |= ^= >>= <<=
 
Special Operators
is  is not
in in not
'''

'''
Syntax of if...else
    if test expression:
        Body of if
    else:
        Body of else

'''

age = int(input("Whats your age: "))
if age < 18:
    print("You cannot vote, thank god")
else:
    print("Yes you can vote \n #Vote for MODI")

# Looping

# while
i = 1
while i < 10:
    print(i)
    i += 1

# for
for x in range(1, 10, 1):
    print(x)

# Looping through a dictionary : Looping + Conditions

flavour = input("choose flavour: ")
for i in (dictionary.get("Ice-creams")):
    if i.get("flavour").__eq__(flavour):
        print("Company: " + i.get("company") + " \n  Price: " + str(i.get("price")))
    else:
        print("Flavour Doesn't exist")
        break
