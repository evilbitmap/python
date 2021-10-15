import random as rnd
import msvcrt
import os

#definice
randomNumberUser = 0
randomNumberPC = 0
userPoints = 0
computerPoints = 0

#command pro vymazání console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#příkáz pro čekání na jakejkoliv input key
def wait():
    msvcrt.getch()

#vygeneruje náhodný číslo
def generateRandomNum():
    global randomNumberUser
    global randomNumberPC

    randomNumberPC = rnd.randint(1,6)
    randomNumberUser = rnd.randint(1,6)
    
#tělo programu, ukazuje body, nahodný čísla a čeká na input
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
    if(userInput == "commands"):
        commands()

    else:
        generateRandomNum()
        ifLowerOrHigher()


#určuje kdo vyhrál
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

#uživatelské příkazy
def commands():
    global userPoints
    global computerPoints
    cls()
    print("commands:")
    print("         reset ; exit")
    print("type back to go back")
    userinput = input(">")
    if(userinput == "reset"):
        userPoints = 0
        computerPoints = 0
        main()
    elif(userinput == "exit"):
        exit()


if (__name__ == "__main__"):
    main()
