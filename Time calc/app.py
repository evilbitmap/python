from tkinter import *
# window
root = Tk()
frame = Frame(root)
frame2 = Frame(root)
root.title("swag martin pek")
root.geometry("650x200")
root.resizable(False, False)
font = ("Comic Sans MS", 8)


def checkTextBoxs():
    if(TextboxSekundy.get() == ""):
        TextboxSekundy.insert(0, 0)
    if(TextboxMinuty.get() == ""):
        TextboxMinuty.insert(0, 0)
    if(TextboxHodiny.get() == ""):
        TextboxHodiny.insert(0, 0)

    converter(int(TextboxHodiny.get()), int(TextboxMinuty.get()), int(TextboxSekundy.get()))


def converter(h, m, s):
    # sekundy
    if(s <= 59):
        labelSekundy.config(text=s)
    elif(s > 59):
        sZbytek = s % 60
        labelSekundy.config(text=sZbytek)
        minuta = (s - sZbytek) / 60
        minuta = minuta + m
        labelMinuty.config(text=minuta)
        m = minuta
    # minuty
    if(m <= 59):
        labelMinuty.config(text=m)
    elif(m > 59):
        mZbytek = m % 60
        labelMinuty.config(text=mZbytek)
        hodina = (m - mZbytek) / 60
        hodina = hodina + h
        labelhodiny.config(text=hodina)
        h = hodina
    # hodiny
    if(h <= 59):
        labelhodiny.config(text=h)
    elif(h > 59):
        #kdykoliv se muze pridat na dny...
        labelhodiny.config(text=h)


def main():
    print("bruh main")


if __name__ == "__main__":
    main()

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
Label(frame2, text="Výsledek", font=("Comic Sans MS", 16), anchor=CENTER).grid(row=1)
# dolní část

# Label Hodiny výsledek
Label(frame2, text="Hodiny: ").grid(row=2, column=0)
labelhodiny = Label(frame2, text="", font=font)
labelhodiny.grid(row=2, column=1)

# Label Minuty výsledek
Label(frame2, text="Minuty: ").grid(row=3, column=0)
labelMinuty = Label(frame2, text="", font=font)
labelMinuty.grid(row=3, column=1)

# Label Sekundy výsledek
Label(frame2, text="Sekundy: ").grid(row=4, column=0)
labelSekundy = Label(frame2, text="", font=font)
labelSekundy.grid(row=4, column=1)

# button převést
Button(frame2, text="převést", command=checkTextBoxs).grid(row=5)

frame.pack()
frame2.pack()
root.mainloop()
