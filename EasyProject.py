from EasyProjects.BinarySearchAlgorithm import BinarySearchAlgorithm
from EasyProjects.DesktopNotifier import DesktopNotifier
from EasyProjects.DiceSimulator import DiceSimulator
from EasyProjects.EmailSlicer import EmailSlicer
from EasyProjects.LinearSearchAlgo import LinearSearchAlgorithm
from EasyProjects.NumberGuessing import NumberGuessing
from EasyProjects.PythonWebsiteBlocker import PythonWebsiteBlocker
from EasyProjects.StoryGenerator import StoryGenerator
from EasyProjects.YoutubeVideosDownloader import YoutubeVideosDownloader
from Lib.bcolors import bcolors
from EasyProjects.instabot import InstaBot
from EasyProjects.Calculator import Calculator
from EasyProjects.webscraping import WebScraping


print("Welcome to Harshit's Easy Projects\nThese are all the projects you can visit")
projects = ["Exit Program", "Dice Simulator", "Email Slicer", "Number Guesssing", "Insta Bot",
            "Linear Search Algorithm", "Binary Search Algorithm", "Desktop Notifier", "Story Generator",
            "Python Website Blocker", "Youtube Videos Downloader","Calculator", "Web Scraper"]

for i in range(projects.__len__()):
    print(str(i) + " " + projects[i])
try:
    a = 1
    while a == 1:
        projectchoosed = int(input("Choose the project you want to visit by typing the Project index: "))
        if projectchoosed == 0:
            break
        elif projectchoosed == 1:
            DiceSimulator()
        elif projectchoosed == 2:
            EmailSlicer()
        elif projectchoosed == 3:
            NumberGuessing()
        elif projectchoosed == 4:
            try:
                print(bcolors.HEADER + "Welcome to InstaBot" + bcolors.ENDC)
                username = input("Choose Username: ")
                password = input("Choose Password: ")
                myBot = InstaBot(username, password)
                myBot.get_unfollowers()
            except:
                print(bcolors.FAIL + "Error" + bcolors.ENDC)
        elif projectchoosed == 5:
            LinearSearchAlgorithm()
        elif projectchoosed == 6:
            BinarySearchAlgorithm()
        elif projectchoosed == 7:
            DesktopNotifier()
        elif projectchoosed == 8:
            StoryGenerator()
        elif projectchoosed == 9:
            PythonWebsiteBlocker()
        elif projectchoosed == 10:
            YoutubeVideosDownloader()
        elif projectchoosed == 11:
            Calculator()
        elif projectchoosed == 12:
            WebScraping()
        else:
            print(bcolors.FAIL + "Please choose an integer only from the Project index" + bcolors.ENDC)
except:
    print(bcolors.FAIL + "Please choose an integer only" + bcolors.ENDC)

exit(0)
