def nob(n):
    ones = 0
    zeros = 0

    while n > 0:
        if n & 1 == 1:
            ones += 1
        else:
            zeros += 1
        n >>= 1

    print("Ones =", ones)
    print("Zeros =", zeros)

number = int(input("Enter your number: "))
nob(number)

