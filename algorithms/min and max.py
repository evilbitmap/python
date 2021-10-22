data = [-6, 179, 5786, -67]

def main():

    global data

    userInputNumberOne = int(input("Start number: "))
    userInputNumberTwo = int(input("End number: "))
    data = [i for i in range(userInputNumberOne, userInputNumberTwo+1)]

    print(data)
    print(f"Biggest number: {max(data)}")
    print(f"Lowest number: {min(data)}")


def Otherway():
    global data
    max_cislo = data[0]

    
    for i in data: #for i in range(len(data))
        if i > max_cislo: # < for min
            max_cislo = i
        

    print("")
    print(f"max: {max_cislo}")
        



if __name__ == "__main__":
    main()
    Otherway()
