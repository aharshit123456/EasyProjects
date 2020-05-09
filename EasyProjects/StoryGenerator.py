# from tkinter import *
import random

from Lib.bcolors import bcolors


def StoryGenerator():
    print(bcolors.HEADER + "Welcome to Story Generator" + bcolors.ENDC)
    user_name = input("What is your Name: ")

    names = ["Cliff", "Jenette", "Epifania", "Effie", "Bulah", "Albina", "Joeann", "Antonietta", "Kenda", "Raymon",
             "Jacquie", "Rubye", "Lenard", "Pedro", "Oretha", "Jacquetta", "Marcie", "Zoraida"]
    places = ["Kelley", "Suzi", "Vivian", "Mayme", "Jacki", "Conception", "Willy", "Ima", "Teodoro", "Dona", "Donn",
              "Earlene", "Patsy", "Irmgard", "Bridget", "Evie", "Elizebeth", "Melany", "Jessia", "Salina"]
    species = ["witch", "droid", "human", "Demon Lord", "ogre"]

    work = ["lawyer", "adventurer", "doctor", "healer", "war front leader", "war leader", "celebrity actor"]

    randomname = random.choice(names)
    randomplaces = random.choice(places)
    randomspecies = random.choice(species)
    randomwork = random.choice(work)

    story1 = "Hello " + user_name + "\n" + bcolors.BOLD + "The Tale of a Young " + randomspecies + bcolors.ENDC + "\n"
    story2 = "by " + user_name + "\n \n This is the story of a young " + randomspecies + " who goes by the name "
    story3 = randomname + ". \n He is loved by everyone in the city of " + randomplaces + "." + "He works as a "
    story4 = randomwork + ". \n"

    print(story1 + story2 + story3 + story4)


    # app = Tk()
    #
    # # Nameofchar
    # part_text = StringVar()
    # part_label = Label(app, text='Name of the character', font=('bold', 14), pady=20)
    # part_label.grid(row=0, column=0)
    # enterName = Entry(app, textvariable=part_text)
    # enterName.grid(row=0, column=1)
    #
    # # Nameofchar
    # part_text = StringVar()
    # part_label = Label(app, text='Name of the characte r', font=('bold', 14), pady=20)
    # part_label.grid(row=1, column=0)
    # enterName = Entry(app, textvariable=part_text)
    # enterName.grid(row=1, column=1)
    #
    # # Nameofchar
    # part_text = StringVar()
    # part_label = Label(app, text='Name of the character', font=('bold', 14), pady=20)
    # part_label.grid(row=2, column=0)
    # enterName = Entry(app, textvariable=part_text)
    # enterName.grid(row=2, column=1)
    #
    # # Nameofchar
    # part_text = StringVar()
    # part_label = Label(app, text='Name of the character', font=('bold', 14), pady=20)
    # part_label.grid(row=3, column=0)
    # enterName = Entry(app, textvariable=part_text)
    # enterName.grid(row=3, column=1)
    #
    # app.title("Story Generator")
    # app.geometry('600x300')
    #
    # app.mainloop()
