from tridy import tridy

def PrintData():
    for trida in tridy:
        print(f'Class: {trida["class"]} ; Amount: {trida["amount"]} ; Any notes: {trida["notes"]}')


def PrintAllClasses():
    for trida in tridy:
         print(f'Class: {trida["class"]}')

def PrintSpecificClass(x):
    print(f'Class: {tridy["class"]} ; Amount: {tridy["amount"]} ; Any notes: {tridy["notes"]}')

def  PrintSpecificClassWithNumber():
    for x in range(len(tridy)):
        print(f'{x}-Class: {tridy[x]["class"]}')