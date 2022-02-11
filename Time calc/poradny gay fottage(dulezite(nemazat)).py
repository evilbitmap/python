Sec.get = textbox Sekunda

def převést():
    if(Sec.get() > 59):
        sekunda = Sec.get() % 60
        minuta = (Sec.get() - sekunda) / 60

        print("min" + str(minuta))
        print("sec" + str(sekunda))
