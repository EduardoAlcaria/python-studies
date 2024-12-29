def double(c = 0, f=False):
    if f == True:
        return coin(c*2)
    else:
        return c * 2
def half(c = 0, f=False):
    if f == True:
        return coin(c / 2)
    else:
        return c / 2
def increase(c = 0, p = 0, f=False):
    if f == True:
        return coin(c + ((p/100)*c))
    else:
        return coin(c + ((p/100)*c))
def decrease(c = 0, p = 0, f=False):
    if f == True:
        return coin(c - ((p/100)*c))
    else:
        return coin(c - ((p/100)*c))
def coin(c = 0):
    return f"${c:.2f}".replace('.', ',')
def line(msg):
    l = len(msg) + 30
    print("~" * l)
    print(f"{' '*15}{msg}")
    print("~" * l)
def summary(n, pA, pD):
    line("PRICE SUMMARY")
    print(f"{'Analized price:  ':}\t{coin(n)}")
    print(f"{'Price times 2:   '}\t{double(n, True)}")
    print(f"{'half the price: ':}\t{half(n,True)}")
    print(f"with {pA}% of augment: \t{increase(n, pA,True)}")
    print(f"with {pD}% of reduction:\t{decrease(n, pD,True)}")
    print("~"*43)