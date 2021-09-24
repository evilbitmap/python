from printdata import PrintSpecificClassWithNumber
from printdata import PrintSpecificClass
from printdata import PrintData
from printdata import PrintAllClasses
from tridy import tridy


def menu():
    print("1: print all classes")
    print("2: print specific class")
    choice=int(input(": "))
    match(choice):
        case 1:
            PrintData()
        case 2:
            print("choose class...")
            for x in tridy:
                PrintSpecificClassWithNumber()
                choiceSpecificClass=int(input(": "))
                if choiceSpecificClass in tridy[choiceSpecificClass]["class"]:
                    PrintSpecificClass(choiceSpecificClass)






def main():
    print("menu \n")


if __name__ == "__main__":
    main()
    menu()