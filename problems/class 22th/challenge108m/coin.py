def double(c = 0):
    return c * 2
def half(c = 0):
    return c / 2
def increase(c = 0, p = 0):
    return ((p/100)*c) + c
def decrease(c = 0, p = 0):
    return c - ((p/100)*c) 
def coin(c):
    return f"${c:.2f}".replace('.', ',')