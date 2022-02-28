from tkinter import *
from tkinter import messagebox
# window
# root
root = Tk()
# framy - na layout
frame = Frame(root)
frame2 = Frame(root)
# jméno okna
root.title("Time converter")
# velikost okna
root.geometry("650x225")
# uživatel nebude moct měnit velikost okna
root.resizable(False, False)
# font
font = ("Comic Sans MS", 8)


def checkTextBoxs():
    if(TextboxSekundy.get() == ""):
        TextboxSekundy.insert(0, 0)
    if(TextboxMinuty.get() == ""):
        TextboxMinuty.insert(0, 0)
    if(TextboxHodiny.get() == ""):
        TextboxHodiny.insert(0, 0)
        # Zkusí vyvolat funkci
    try:
        convert(float(TextboxHodiny.get()), float(TextboxMinuty.get()), float(TextboxSekundy.get()))
        # pokud bude špatnej input (ValueError) tak...
    except(ValueError):
        messagebox.showerror("ERROR: Wrong input!", "Prosím zadej validní input")

def clear():
    labelSekundy.config(text=0.0)
    labelMinuty.config(text=0.0)
    labelhodiny.config(text=0.0)


def convert(h, m, s):
    # aby číslo bylo bez decimálního čísla musíme ho vykrátit 60
    # potom se zjistí zbytek
    m = m * 60
    mZbytek = m % 60

    # do sekund se přídá zbytek minut
    # a potom se zjistí zbytek
    s = s + mZbytek
    sZbytek = s % 60

    # pokud sekunda bude větší než 59 tak se to přídá
    # do m2
    m2 = (s - sZbytek) / 60
    # tady se zjistí kolik je minuta a přídá se m2
    m = (m - mZbytek) / 60 + m2

    # číslo nesmí bejt decimální proto
    # a zjistí se zbytek
    h = h * 60
    hZbytek = h % 60

    # do minut se přídá zbytek hodin
    # a potom se zjistí zbytek u minut
    m = m + hZbytek
    mZbytek = m % 60

    # pokud minuta bude větší než 59 tak se to přídá
    # do h2
    h2 = (m - mZbytek) / 60
    # a tady se zjistí kolik je hodina a přidá se h2
    h = (h - hZbytek) / 60 + h2

    # musí se zjistit zbytek aby se neukoazovali 60- ky
    s = s % 60
    m = m % 60
    h = h % 60

    # vypiš čísla
    labelSekundy.config(text=s)
    labelMinuty.config(text=m)
    labelhodiny.config(text=h)


# Label main
labelMain = Label(root, text="Převod času", font=("Comic Sans MS", 16), anchor=CENTER)
labelMain.pack()

# Label + Textbox Hodiny
Label(frame, text="Hodiny: ", font=font).grid(row=0, column=0)
TextboxHodiny = Entry(frame, font=font)
TextboxHodiny.grid(row=0, column=1)

# Label + Textbox Minuty
Label(frame, text="Minuty: ", font=font).grid(row=0, column=2, padx=10)
TextboxMinuty = Entry(frame, font=font)
TextboxMinuty.grid(row=0, column=3)

# Label + Textbox Sekundy
Label(frame, text="Sekundy: ", font=font).grid(row=0, column=4, padx=10)
TextboxSekundy = Entry(frame, font=font)
TextboxSekundy.grid(row=0, column=5)

# Mezera
Label(frame2, text="Výsledek", font=("Comic Sans MS", 16), anchor=CENTER).grid(row=0, column=0)
# dolní část

# Label Hodiny výsledek
Label(frame2, text="Hodiny: ").grid(row=1, column=0)
labelhodiny = Label(frame2, text="0.0", font=font)
labelhodiny.grid(row=1, column=1)

# Label Minuty výsledek
Label(frame2, text="Minuty: ").grid(row=2, column=0)
labelMinuty = Label(frame2, text="0.0", font=font)
labelMinuty.grid(row=2, column=1)

# Label Sekundy výsledek
Label(frame2, text="Sekundy: ").grid(row=3, column=0)
labelSekundy = Label(frame2, text="0.0", font=font)
labelSekundy.grid(row=3, column=1)

# button převést
Button(frame2, text="Převést", command=checkTextBoxs).grid(row=4, column=0)

# button clear
Button(frame2, text="Clear", command=clear).grid(row=5, pady=10)


def main():
    frame.pack()
    frame2.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
