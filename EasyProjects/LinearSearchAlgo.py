from Lib.bcolors import bcolors

str = ""
strarray = []


def LinearSearchAlgorithm():
        print(bcolors.HEADER + "Welcome to Linear Search Algorithm" + bcolors.ENDC)
        string:int = int(input("Enter string to lookup: "))
        strarray = [1, 3, 6, 7, 10, 23, 343, 3433, 34334, 65655, 99999, 343433, 665656, 898999, 3434344, 4565665, 5656565]
        # strarray = [input("Enter Array: ")]
        i = 0
        found = False
        for i in range(len(strarray)):
            if (string == strarray[i]):
                print("Your string is at " + (i).__str__() + " postion in the array")
                found = True
                break
        if not found: print("Not Found")
