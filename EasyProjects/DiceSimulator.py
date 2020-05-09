from random import randint

# The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the
# user can play again and again to get a number from the dice until the user decides to quit the program.
from Lib.bcolors import bcolors


def DiceSimulator():
    print(bcolors.HEADER + "Welcome to Dice Simulator"+ bcolors.ENDC)
    a = 1
    while a == 1:
        value = input("Press k for another turn or press e for exiting: ")
        if value == "e":
            break
        elif value == "k":
            print(randint(0, 6))
        else:
            print("Value not acceptable")
