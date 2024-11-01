s = float(input('Type a salary: '))
aug = s * (10/100)
if s <= 1250:
    print('your new salary is 15 persent bigger\nand it will be ${}'.format((s * 15/100) + s))
else:
    print('your new salary is 10 persent bigger\nand it will be ${}$'.format((s * 10/100) + s))
