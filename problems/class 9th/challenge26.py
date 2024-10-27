string = str(input('Type something: ')).strip().lower()
print('There is {} letters A'.format(string.lower().count('a')))
print('The first letter A are in the spot {}'.format(string.find('a') + 1))
print('The last letter A are in the spot {}'.format(string.rfind('a') + 1)) 