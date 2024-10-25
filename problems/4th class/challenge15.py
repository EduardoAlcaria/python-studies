days = int(input('How many days have you rent the car? '))
km = float(input('How many km have you riden? '))
print('You must pay ${:.2f}'.format(days * 60 + 0.15 * km))