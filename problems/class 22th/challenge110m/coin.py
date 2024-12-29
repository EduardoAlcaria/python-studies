def double(c, f=False):
    if f == True:
        return coin(c*2)
    else:
        return c * 2
def half(c, f=False):
    if f == True:
        return coin(c / 2)
    else:
        return c / 2
def increase(c, p, f=False):
    if f == True:
        return coin(((p/100)*c) + c)
    else:
        return ((p/100)*c) + c
def decrease(c, p, f=False):
    if f == True:
        return coin(c - ((p/100)*c))
    else:
        return c - ((p/100)*c)
def coin(c):
    return f"${c}"
def line(msg):
    l = len(msg) + 30
    print("~" * l)
    print(f"{" "*15}{msg}")
    print("~" * l)
def summary(n, pA, pD):
    line("PRICE SUMMARY")
    print(f"{'Analized price:  ':<10}{coin(n):>15}")
    print(f"{'Price times 2:   ':<10}{double(n, True):>15}")
    print(f"{'half the price: ':<10}{half(n,True):>15}")
    print(f"with {pA}% of augment: {increase(n, pA,True):>11}")
    print(f"with {pD}% of reduction:{decrease(n, pD,True):>9}")
    print("~"*43)



