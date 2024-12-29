def readmoney(msg):
    while True:
        m = input(msg)
        if m.isnumeric():
            m = int(m)
            return m
        if m.isdecimal():
            m = float(m)
            return m
        else:
            print(f"\033[1;31mERROR, \'{m}\' is an invalid price\033[m")