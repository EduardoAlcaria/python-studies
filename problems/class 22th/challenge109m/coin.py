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