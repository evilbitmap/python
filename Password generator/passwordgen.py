import random
import string
def genpass(PassLenght):
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits,k=PassLenght))

def main():
        print("".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits,k=5)))



if (__name__ == "__main__"):
    print("___")
    print("choose a lenght...")
    print("___")
    PasslenghtInput=int(input(">"))
    print("___")
    print("choose a amount of passwords to generate...")
    print("___")
    PassAmountInput=int(input(">"))
    for i in range(int(PassAmountInput)):
        print(genpass(int(PasslenghtInput)))
    
    print("---------------------------------------")
    
    for x in range(PassAmountInput):
        print(f'{x+1} {genpass(PasslenghtInput)}')
