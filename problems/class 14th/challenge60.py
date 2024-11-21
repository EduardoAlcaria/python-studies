n = int(input("Enter a number: "))
count = n
f = 1
while count != 0:
    print(f"{n}x{count} ",end="")
    f *= count
    count -= 1
print(f"\nthe factorial is {f}")