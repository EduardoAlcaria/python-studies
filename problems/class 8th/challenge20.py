from random import shuffle
n1 = str(input('1st name: '))
n2 = str(input('2nd name: '))
n3 = str(input('3th name: '))
n4 = str(input('4th name: '))
names = [n1, n2, n3, n4]
shuffle(names)
print('the order will be\n{}'.format(names))
