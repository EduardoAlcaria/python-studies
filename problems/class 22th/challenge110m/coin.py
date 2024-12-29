def double(c = 0, f=False):
    if f == True:
        res = coin(c*2)
        return res
    else:
        res = c * 2
        return res
def half(c = 0, f=False):
    if f == True:
        res =  coin(c / 2)
        return res
    else:
        res = c / 2
        return res
def increase(c = 0, p = 0, f=False):
    if f == True:
        res = coin(c + ((p/100)*c))
        return res
    else:
        res = coin(c + ((p/100)*c))
        return res
def decrease(c = 0, p = 0, f=False):
    if f == True:
        res = coin(c - ((p/100)*c))
        return res
    else:
        res = coin(c - ((p/100)*c))
        return res
def coin(c = 0):
    res = f"${c:.2f}".replace('.', ',')
    return res
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