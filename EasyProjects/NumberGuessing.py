from random import randint
from Lib.bcolors import bcolors
from tkinter import *


def GUI():
    app = Tk()

    part_text = StringVar()
    part_label = Label(app, text='How many attempts do you wanna play: ', font=('bold', 14), pady=20)
    part_label.grid(row=0, column=0)
    enterName = Entry(app, textvariable=part_text)
    enterName.grid(row=0, column=1)

    app.title("Guess the Number")
    app.geometry('600x300')

    app.mainloop()


def NumberGuessing():
    isSuccesful = False
    a = 1
    while a == 1:
        try:
            print(bcolors.HEADER + bcolors.UNDERLINE + "Time To Choose a Random Number" + bcolors.ENDC)
            print(
                bcolors.BOLD + "A program which randomly chooses a number to guess and then the user will have a few chances to guess the "
                               "\nnumber. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the "
                               "\none you have guessed." + bcolors.ENDC)
            print("Type 0 to exit")
            noofattempts = int(input("How many attempts do you wanna play: "))
            if (noofattempts == 0):
                break
            else:
                rangemax = int(input("What should be the max value of the random number: "))
                if (rangemax == 0):
                    break
                else:
                    randInt = randint(0, rangemax)
                    for i in range(noofattempts):
                        attempt = int(input("Guess the number: "))
                        chancesLeft = "You have " + str(noofattempts - (i + 1)) + " more chances"

                        if (attempt > randInt):
                            print("The number is smaller than what you chose.")
                            isSuccesful = False
                            print(chancesLeft)
                        elif (attempt < randInt):
                            print("The number is greater than what you chose.")
                            isSuccesful = False
                            print(chancesLeft)
                        elif (attempt == randInt):
                            print("Congratulations, your guess was correct, " + str(attempt) + " is the correct number")
                            isSuccesful = True
                            break
                        else:
                            print("Error")
                            isSuccesful = False
                            quit(0)
                    if not isSuccesful:
                        print("HaHa!! you lose. The correct number was " + str(randInt))
        except:
            print("Only integers!!")
