y=1
x=0
while(y):
    c=input("enter number:")
    x += int(c)
    print(x)
    if(c == "00"):
        y=0
        print("EXIT CODE: 00")
        exit