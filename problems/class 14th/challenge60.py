from math import factorial
n = int(input("Enter a number: "))
count = n
while count != 0:
    print(f"{n}x{count} ",end="")
    count -= 1
print(f"\nthe factorial is {factorial(n)}")