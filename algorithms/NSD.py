def main():
    print("...")
    u=int(input("number one:"))
    w=int(input("number two:"))

    while(w != 0):
        r = u % w
        u = w
        w = r
    print(u)




if __name__ == "__main__":
    main()
