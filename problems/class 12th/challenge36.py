houseValue = int(input('Type the house price $ '))
salary = float(input('How much do you earn $ '))
years = int(input('In how many years you will pay: '))

times =  houseValue / (years * 12)
per = salary * 0.3


if times < per:
    print('\nyour loan has been \033[1;32mAPPROVED\033[0m \nyou will pay in {:.2f}$ per month\n'.format(times))
elif times > per:
    print('your loan has been \033[1;31mDENNIED\033[0m\nyour salary doesnt cover the foan')
else:
    print('good bye')