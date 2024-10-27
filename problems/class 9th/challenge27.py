name = str(input('Type a name: ')).strip()
splited = name.split()
print('your first name is', splited[0])
print('your last name is', splited[len(splited) - 1])