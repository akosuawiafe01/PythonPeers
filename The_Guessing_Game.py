#This is  a Mini Guessing game

from random import *

def generateNumber():
    return randint(0,100)



print("******\t\t\t Hey there, welcome to the Mini Guessing Game with AK *****\t\t\t\n")


print("Enter your name: \t")
name = input()

print("Hello ", str(name), ", I am searching for a number between 0 and 100, please help me find it...\n")

print("Kindly enter a number in the range given above(0 to 100): ")
number = input()


randomNumber = generateNumber()

if number == randomNumber:
        print("Yaaay, you found it right")
elif int(number) < (randomNumber-5):
        print("Hm, you almost found it")
elif int(number) > (randomNumber+10):
        print("Oh no, your guess was too wide")
    

print("I was searching for ", randomNumber)
print('\n Thanks for playing with me, see you next time')