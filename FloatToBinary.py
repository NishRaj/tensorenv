x = float(input("Enter a number between 0 and 1:"))
p=0
while (2**p)*x % 1 != 0:
    p += 1
num = int((2**p)*x)

