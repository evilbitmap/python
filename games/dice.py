import random as rnd
import msvcrt
import os

#definice
randomNumberUser = 0
randomNumberPC = 0
userPoints = 0
computerPoints = 0
gamesPlayed = 0
userProcentage = 0
computerProcentage = 0

#command pro vymazání console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#příkáz pro čekání na jakejkoliv input key
def wait():
    msvcrt.getch()

def savefile():
    global userPoints
    global computerPoints
    global userProcentage
    global computerProcentage
    f = open("score (dice.py).txt", "w")
    f.write(f"your score: {userPoints} ; computer score: {computerPoints} \n {userProcentage} ; {computerProcentage} \n games played: {gamesPlayed}")
    f.close

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
    print(f"games played: {gamesPlayed}")
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

def calculateProcentage():
    global userPoints
    global computerPoints
    global gamesPlayed
    global userProcentage
    global computerProcentage

    userProcentage = userPoints / gamesPlayed
    userProcentage = userProcentage * 100
    computerProcentage = computerPoints / gamesPlayed
    computerProcentage = computerProcentage * 100




#určuje kdo vyhrál
def ifLowerOrHigher():
    global userPoints
    global computerPoints
    global gamesPlayed

    if(randomNumberUser > randomNumberPC):
        userPoints += 1
        gamesPlayed += 1
        calculateProcentage()
        main()

    elif(randomNumberUser < randomNumberPC):
        computerPoints += 1
        gamesPlayed += 1
        calculateProcentage()
        main()

    elif(randomNumberUser == randomNumberPC):
        gamesPlayed += 1
        calculateProcentage()
        main()

#uživatelské příkazy
def commands():
    global userPoints
    global computerPoints
    cls()
    print("commands:")
    print("         reset ; exit ; save score")
    print("type back to go back")
    userinput = input(">")
    if(userinput == "reset"):
        userPoints = 0
        computerPoints = 0
        main()
    
    elif(userinput == "save score"):
        savefile()
        main()

    elif(userinput == "exit"):
        exit()
    


if (__name__ == "__main__"):
    main()
