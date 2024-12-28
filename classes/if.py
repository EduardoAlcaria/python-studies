n1 = float(input('Type the 1st grade: '))
n2 = float(input('Type the 2nd grade: '))
m = (n1+n2)/2
print('your minimal grade are {:.1f}'.format(m))
if m >= 6.0:
    print('Your minimal grade is great')
else:
    print('Your minimal grade is the worse')