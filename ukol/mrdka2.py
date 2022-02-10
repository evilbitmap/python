from asyncio.windows_events import NULL
from cProfile import label
from contextlib import nullcontext
from ctypes import resize
from operator import truediv
import tkinter as tk
from tkinter import *
import qrcode
from PIL import ImageTk, Image
import os.path
import os
import time

#data z textboxu
def GetInputFromTextbox():
    global input
    input = Textbox.get("1.0", tk.END)


#generace qr code
def GenQRcode():
    GetInputFromTextbox()

    #qr code maker 3000
    qr = qrcode.QRCode()
    qr.add_data("brush")
    img = qrcode.make(input)
    
    #
    #zkontroluj jestli qrcode1 existuje pokud ne vytvor qrcode2 a vymaz qrcode1 a naopak
    #
    if not (os.path.isfile("qrcode1.png")):
        img.save("qrcode1.png")
        os.remove("qrcode2.png")
    else:
        os.remove("qrcode1.png")
        img.save("qrcode2.png")

    ShowImage()


#image
def ShowImage():
    path1 = r"qrcode1.png"
    path2 = r"qrcode2.png"

    while not os.path.exists(path1 or path2):
        time.sleep(1)

    if os.path.isfile(path1 & path2):
        if (os.path.isfile("qrcode1.png")):
            resize_image = path1.resize((100, 100))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img

        elif (os.path.isfile("qrcode2.png")):
            resize_image = path2.resize((100, 100))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img

        label1.pack()



#window name
root = tk.Tk(className="qr code")

#window size
root.geometry("500x200")

#label
labelMain = tk.Label(root, text="qr code gen")
labelMain.config(font=("Arial", 16))

#textbox
Textbox = tk.Text(root, height=1, width=60)

#button
buttonCreate = tk.Button(root, text="Generuj", command=GenQRcode)


def main():
    #pack
    labelMain.pack()
    Textbox.pack()
    buttonCreate.pack()

    #start
    root.mainloop()


if __name__ == "__main__":
        main()
