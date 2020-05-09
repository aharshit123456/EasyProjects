import tkinter as tk
from tkinter import messagebox
from Lib.bcolors import bcolors
from time import sleep


def DesktopNotifier():
    print(bcolors.HEADER + "Welcome to Desktop Notifier" + bcolors.ENDC)

    while True:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Pay Attention", "You gay boi")
        if input("Do you want to close(y or n): ") == "y":
            break
        sleep(20)


