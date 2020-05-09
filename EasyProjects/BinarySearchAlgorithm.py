from Lib.bcolors import bcolors

integerx = 0
strarray = [""]


def BinarySearchAlgorithm():
    print(bcolors.HEADER + "Welcome to Binary Search Algorithm" + bcolors.ENDC)
    integerx: int = int(input('Enter int to lookup: '))
    strarray = [1, 3, 6, 7, 10, 23, 343, 3433, 34334, 65655, 99999, 343433, 665656, 898999, 3434344, 4565665, 5656565]
    l = 0
    u = strarray.__len__()
    isSuccess = False
    for l in range(len(strarray)):
        mid = (l + u) // 2
        if integerx == strarray[mid]:
            print("Found at " + str(mid))
            isSuccess = True
            break
        else:
            if strarray[mid] > integerx:
                u = mid
            else:
                l = mid
    if not isSuccess:
        print("Not Found in list")