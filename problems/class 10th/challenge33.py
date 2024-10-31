a = int(input('Type the 1st number: '))
b = int(input('Type the 2nd number: '))
c = int(input('Type the 3th number: '))
low = a
if b<a and b<c:
    low = b
if c<a and c<b:
    low = c


high = a
if b>a and b>c:
    high = b
if c>b and c>a:
    high = c


print('the lowest number is {}'.format(low))
print('the highest number is {}'.format(high))

