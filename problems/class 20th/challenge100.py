from random import randint
num = list()
def rannum():
    print(f"Generating 5 numbers: ",end=" ")
    for c in range(5):
        r = randint(0, 10)
        print(f"{r}", end=" ")
        num.append(r)
    print("READY")
def sEven(n):
    s = 0
    print(f"adding {num} we have ",end="")
    for c in n:
        if c % 2 == 0:
            s += c
    print(f"{s}",end=" ")
    print()
rannum()
sEven(num)