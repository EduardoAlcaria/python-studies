def fact(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show == True:
        for c in range(n, 0, -1):
            print(f"{c} x ", end="")
            if c == 1:
                print("= ",end="")
        return f
    else:
        return f
print(fact(5, show=True))
print(fact(5, show=False))