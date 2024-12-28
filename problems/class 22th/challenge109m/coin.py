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