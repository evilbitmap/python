x = int(input("Zadej číslo: "))
match x:
    case 10:
        print("x je 10")
    case 20:
        print("x je 20")
    case 0:
        print("ty jsi nula")
    case _:
        print("TOHLE JE DEAFULT KOŘEN")