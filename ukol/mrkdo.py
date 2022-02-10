from dis import show_code
import os.path
import time
import tkinter as tk
import qrcode
import PIL


#window name
root = tk.Tk(className="qr code")
#window size
root.geometry("500x500")

#label
labelMain = tk.Label(root, text="qr code gen")
labelMain.config(font=("Arial", 16))
labelMain.pack()

#textbox
Textbox = tk.Text(root, height=1, width=60)
Textbox.pack()

#data z textboxu
def GetInputFromTextbox():
    global input
    input = Textbox.get("1.0", tk.END)


#generace qr code
def GenQRcode():
    GetInputFromTextbox()
    qr = qrcode.QRCode()
    qr.add_data("brush")
    img = qrcode.make(input)
    img.save("qrcode.png")

    ShowImage()


#button
buttonCreate = tk.Button(root, text="Generuj", command=GenQRcode)
buttonCreate.pack()

#image
def ShowImage():
    print("show img")
    qrcodeimage = tk.PhotoImage(file=r"qrcode.png")

    while not os.path.exists("qrcode.png"):
        time.sleep(1)
    if os.path.isfile("qrcode.png"):
        imagecanavs = tk.Canvas(root, width=250, height=250)
        imagecanavs.create_image(250,250,image=qrcodeimage)
        imagecanavs.pack()




#start
root.mainloop()
