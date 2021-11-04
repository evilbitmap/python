def main():
    print("...")
    u=int(input("number one:"))
    w=int(input("number two:"))

    while(w != 0):
        #"r" vyjde zbytek
        r = u % w

        #"u" se bude = w což je to větší číslo
        u = w

        #a "w" se bude rovnat ten zbytek a pokud to bude 0 tak print "u"
        w = r

    print(u)
    print("...")




if __name__ == "__main__":
    main()
