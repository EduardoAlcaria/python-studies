price = float(input('how much have you spent $'))
choise = int(input('You want to pay with\n[1] cash\n[2] in cash with credit card\n[3] in 2 times \n[4] in 3 times or more\n>'))

if choise == 1:
    print('You will pay {:.2f}$'.format(price - (price * 10/100)))
elif choise == 2:
    print('You will pay {:.2f}$'.format(price - (price * 5/100)))
elif choise == 3:
    print('You will pay the same price of {:.2f}$ in 2x of {}$'.format(price, price/2))
elif choise == 4:
    total = price + (price * 20/100)
    times = int(input('How many times? '))
    print('you will pay {:.2f}$ in {}x of {:.2f}$ with 20% charged'.format(total,times,total/times))

else:
    print('invalid payment option')