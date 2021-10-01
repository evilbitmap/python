from printdata import PrintSpecificClass
from printdata import PrintAllClasses
from printdata import PrintNameOfClasses


def menu():
    print("_________________________")
    print("1-> print all classes")
    print("2-> print specific class")
    print("_________________________")
    print("3-> exit")
    print("_________________________")
    choice=int(input(">"))
    match(choice):
        case 1:
            PrintAllClasses()
        case 2:
            while True:
                print("_________________________")
                print("choose a class...")
                PrintNameOfClasses()
                print("_________________________")
                print("00-> back")
                print("_________________________")
                choiceSpecificClass=str(input(">"))
                if choiceSpecificClass == ("00"):
                    return
                else:
                    PrintSpecificClass(choiceSpecificClass)
        case 3:
            exit()
        case _:
            print("please choose a number")

def main():
    menu()


if __name__ == "__main__":
    while True:
        main()
