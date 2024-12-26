def fact(n=0):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f
def isEven(f):
    if f % 2 == 0:
        return True
    else:
        return False
f1 = fact(5)
f2 = fact(4)
f3 = fact()
print(f"{isEven(f1)}, {isEven(f2)}, {isEven(f3)}")
print(f"{f1}, {f2}, {f3}")