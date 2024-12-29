weight = float(input('Whats your weight KG: '))
height = float(input('whats your hieght M: '))

bmi = weight/(height ** 2)
print('your bmi is {:.2f}'.format(bmi))
if bmi < 18.5:
    print('underweight')
elif bmi >= 18.5 and bmi < 25:
    print('healthy weight')
elif bmi >= 25 and bmi < 30:
    print('overweight')
elif bmi >= 30 and bmi < 40:
    print('obesid')
else:
    print('morbid obesity')
