def son(n):
    if number & (1<<(n-1)):
        print("\nSET")
    else:
        print("\nnot SET")
number = int(input("Enter a number: "))
n = int(input(" Enter a bit number: "))
son(number,n)