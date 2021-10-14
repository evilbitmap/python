import random as rnd
import msvcrt
import os


randomNumberUser = 0
randomNumberPC = 0
userPoints = 0
computerPoints = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def wait():
    msvcrt.getch()


def generateRandomNum():
    global randomNumberUser
    global randomNumberPC

    #vygeneruje náhodný číslo
    randomNumberPC = rnd.randint(1,6)
    randomNumberUser = rnd.randint(1,6)
    

def main():
    global userPoints
    global computerPoints
    cls()
    print("--------------------------------")
    print(f"Your points: {userPoints} ; PC points: {computerPoints}")
    print("--------------------------------")
    print(f"Your dice: {randomNumberUser} ; PC dice: {randomNumberPC}")
    print("--------------------------------")
    print("press enter to roll!")
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")
    print("type commands to see commands")
    print("--------------------------------")
    userInput = input("")
    if(userInput == "exit"):
        exit()

    elif(userInput == "reset"):
        userPoints = 0
        computerPoints = 0
        main()
    elif(userInput == "commands"):
        commands()

    else:
        generateRandomNum()
        ifLowerOrHigher()


def ifLowerOrHigher():
    global userPoints
    global computerPoints
    if(randomNumberUser > randomNumberPC):
        userPoints += 1
        main()

    elif(randomNumberUser < randomNumberPC):
        computerPoints += 1
        main()

    elif(randomNumberUser == randomNumberPC):
        main()

def commands():
    print("commands:")
    print("         reset ; exit")
    print("type back to go back")


if (__name__ == "__main__"):
    main()
