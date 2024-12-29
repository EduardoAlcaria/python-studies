def double(c = 0):
    res = c * 2
    return res
def half(c = 0):
    res = c / 2
    return res
def increase(c = 0, p = 0):
    res = ((p/100)*c) + c
    return res
def decrease(c = 0, p = 0):
    res = c - ((p/100)*c)
    return res
def coin(c):
    res =  f"${c:.2f}".replace('.', ',')
    return res