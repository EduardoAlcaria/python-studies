string = str(input('Type something: '))
print('There is {} letters A'.format(string.lower().count('a')))
print('The first letter A are in the spot {}'.format(string.find('a')))
print('The last letter A are in the spot {}'.format(string.rfind('a')))