from datetime import datetime
born = int(input('Enter the year that you was born: '))
age = datetime.now().year - born
gen = int(input('You are [1] boy or [2] woman\n>'))
if gen == 1:
    if age == 18:
        print('You need to sign up for the army NOW!')
    elif age > 18:
        print('its late for sign up to the army\nyou are {} years late'.format(age - 18))
    else:
        print('You will sign up to the army in {} years'.format(18 - age))
else:
    print('You dont need to sign up to the army: ')