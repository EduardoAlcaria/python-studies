from datetime import date
born = int(input('Enter the year that you was born: '))
age = date.today().year - born
if age <= 9:
    print('Classification: Little')
elif age > 9 and age <= 14:
    print('Classification: Middle')
elif age > 14 and age <= 19:
    print('Classification: Big')
elif age > 19 and age <= 20:
    print('Classification: 10+')
else:
    print('Classification: Adult')