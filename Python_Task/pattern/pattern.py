import os
import time


n = 4


def arr1():
    for i in range((n*2)+1):
        for j in range((n*2)+1):
            if (j-i == 4 or i == 4 or j+i == 12):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def arr2():
    for i in range((n*2)+1):
        for j in range((n*2)+1):
            if (j-i == 4 or j == 4 or j+i == 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def arr3():
    for i in range((n*2)+1):
        for j in range((n*2)+1):
            if (i-j == 4 or i == 4 or j+i == 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def arr4():
    for i in range((n*2)+1):
        for j in range((n*2)+1):
            if (i-j == 4 or j == 4 or j+i == 12):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


for i in range(6):
    os.system("cls")
    arr1()
    time.sleep(1)
    os.system("cls")
    arr2()
    time.sleep(1)
    os.system("cls")
    arr3()
    time.sleep(1)
    os.system("cls")
    arr4()
    time.sleep(1)
