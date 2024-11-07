n1 = float(input('Type a mesure: '))
n2 = float(input('Type a mesure: '))
n3 = float(input('Type a mesure: '))

triangule_law = n1 + n2 < n3
print_can = 'it can be a triangule'

if n1 == n2 and n2 == n3 == n1 == n3 and triangule_law:
    print(print_can)
    print('its an equilateral triangule')
elif n1 == n2 and triangule_law: 
    print(print_can)
    print('Its an isosceles triangule')
elif n1 != n2 and n2 != n3 and n3 != n1 and triangule_law:
    print(print_can)
    print('Its a scalene tringule')
else:
    print('it can not be a triangule')