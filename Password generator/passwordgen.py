import random
import string
from tabulate import tabulate


def savefile(x):
        f = open("passwords.txt", "w")
        f.write(tabulate(x, headers=["ID", "Password"], numalign='center', tablefmt='grid'))
        f.close()

def genpass(PassLenght):
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!_.-@?",k=PassLenght))

def main():
        PasslenghtInput=int(input("choose a lenght >"))
        PassAmountInput=int(input("choose a amount of passwords to generate >"))
        passwords = []
        for i in range(PassAmountInput):
            passwords.append([
                i+1,
                genpass(PasslenghtInput)
        ])
        print(tabulate(passwords, headers=["ID", "Password"], numalign='center', tablefmt='grid'))
        savefile(passwords)

if (__name__ == "__main__"):
    main()
