price = int(input('Whats the price $'))
choise = int(input('You want to pay with\n[1] cash\n[2] in cash with credit card\n[3] in 2 times \n[4] in 3 times or more\n>'))

if choise == 1:
    print('You will pay {}$'.format(price - (10/price) * 100))
elif choise == 2:
    print('You will pay {}$'.format(price - (5/price) * 100))
elif choise == 3:
    print('You will pay the same price of {}$'.format(price))
elif choise == 4:
    print('you will pay {}$ with 20% charged'.format((20/price) * 100 + price))