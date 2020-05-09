# The email slicer is a handy program to get the username and domain name
# from an email address. You can customize and send a message to the user with this information.
from Lib.bcolors import bcolors
import csv
import os

#
# def EmailSlicer():
#     print(bcolors.HEADER + "Welcome to Email Slicer" + bcolors.ENDC)
#     a = 1
#     print("Type e to exit")
#
#     while a==1:
#         email = input("What is your email: ")
#         if email.__contains__("@"):
#             emails = email.split("@")
#             print("Name: " + emails[0])
#             print("Domain Name: " + emails[1])
#         elif email == "e":
#             break
#         else:
#             print("Email does is not in the correct format")
#
# def CSVImport():
thisdict: dict = {}
with open('emails.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        email = f'{row["Emails"]}'
        if email.__contains__("@"):
            emails = email.split("@")
            with open('sample.txt', 'a') as file:
                file.write(emails[0] + "\n")
                file.close()
            print(emails[0])
        elif email == "e":
            break
        else:
            print("Email does is not in the correct format")
        line_count += 1
    print(f'Processed {line_count} lines.')
    print(thisdict)
