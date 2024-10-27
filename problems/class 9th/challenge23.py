num = int(input('Type a number (from 0 to 9999): '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{} Ones'.format(u))
print('{} Tens'.format(d))
print('{} Hundreds'.format(c))
print('{} Thousands'.format(m))