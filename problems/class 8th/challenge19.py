from random import choice
n1 = str(input('1st name: '))
n2 = str(input('2nd name: '))
n3 = str(input('3th name: '))
n4 = str(input('4th name: '))
list = [n1, n2, n3, n4]
print('the chosen one is {}'.format(choice(list)))