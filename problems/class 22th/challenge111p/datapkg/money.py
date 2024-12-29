def readmoney(msg):
        while True:
            m = str(input(msg))
            checkdot = m.replace('.', '', 1).isdigit()
            checkcomma = m.replace(',', '', 1).isdigit()
            if checkdot == True:
                return float(m)
                break
            elif checkcomma == True:
                m = m.replace(',', '.')
                return float(m)
                break
            elif m.isnumeric():
                m = int(m)
                return m
                break
            else:
                print(f"\033[1;31mERROR, \'{m}\' is an invalid price\033[m")