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