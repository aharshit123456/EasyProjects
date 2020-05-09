# The email slicer is a handy program to get the username and domain name
# from an email address. You can customize and send a message to the user with this information.
from Lib.bcolors import bcolors


def EmailSlicer():
    print(bcolors.HEADER + "Welcome to Email Slicer" + bcolors.ENDC)
    a = 1
    print("Type e to exit")

    while a==1:
        email = input("What is your email: ")
        if email.__contains__("@"):
            emails = email.split("@")
            print("Name: " + emails[0])
            print("Domain Name: " + emails[1])
        elif email == "e":
            break
        else:
            print("Email does is not in the correct format")
