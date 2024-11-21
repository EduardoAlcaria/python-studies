n = int(input("Enter a number: "))
f = 1
for c in range(n, 0, -1):
    print(f"{n}x{c} ",end="")
    f *= c
print(f"\nthe factorial is {f}")