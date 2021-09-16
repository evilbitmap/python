def min():
    c = x - y
    print(f"{x} - {y} = {c}")
def plus():
    c = x + y
    print(f"{x} + {y} = {c}")
def krat():
    c = x * y
    print(f"{x} * {y} = {c}")
def deleni():
    c = x / y
    print(f"{x} / {y} = {c}")
if(__name__ == "__main__"):
    print("1.plus")
    print("2.mínus")
    print("3.krát")
    print("4.dělení")
    choice = input("(1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
        x=int(input("první číslo: "))
        y=int(input("druhé číslo: "))
    else:
        print("prosím zadejte výběr 1/2/3/4")
    if choice == "1":
        plus()
    if choice == "2":
        min()
    if choice == "3":
        krat()
    if choice == "4":
        deleni()