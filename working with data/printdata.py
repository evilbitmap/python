from tridy import tridy

#vypíše pouze jména tříd
def PrintNameOfClasses():
    for trida in tridy:
         print(f'Class: {trida["class"]}')

#vypíše všechny třídy co jsou ve tridy.py
def PrintAllClasses():
    for trida in tridy:
         print(f'Class: {trida["class"]} ; Amount: {trida["amount"]} ; Any notes: {trida["notes"]}')

#vypíše uživatelsky určenou třídu
def PrintSpecificClass(x):
    print(f'Class: {tridy[x]["class"]} ; Amount: {tridy[x]["amount"]} ; Any notes: {tridy[x]["notes"]}')

def PrintSpecificClass(choiceSpecificClass):
    for t in tridy: 
        if(choiceSpecificClass == t["class"]):
            print(f'Class: {t["class"]} ; Amount: {t["amount"]} ; Any notes: {t["notes"]}')
