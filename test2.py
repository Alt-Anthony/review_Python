def main():
    x:int = int(input("What's x?"))
    print("x squared is ", square(x))


def square(n:int):
    return pow(n,2)
    

main()