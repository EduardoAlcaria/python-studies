age = int(input('Enter an age: '))

if age <= 9:
    print('Little')
elif age > 9 and age <= 14:
    print('middle')
elif age > 14 and age <= 19:
    print('big')
elif age > 19 and age <= 20:
    print('10+')
else:
    print('adult')