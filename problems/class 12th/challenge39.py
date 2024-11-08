from datetime import datetime
born = int(input('Enter the year that you was born '))
age = datetime.now().year - born
if age == 18:
    print('You need to sign up for the army')
elif age > 18:
    print('its late for sign up to the army')
else:
    print('You will sign up to the army in {} years'.format(18 - age))