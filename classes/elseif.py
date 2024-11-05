name = str(input('Whats your name: ')).strip().capitalize()

if name == 'Eduardo':
    print('Nice to meet you {}'.format(name))
elif name == 'Maria' or name == 'Pedro' or name == 'Ana':
    print('What a beautiful name')
elif name in 'Claudia Creuza':
    print('Your name is so common')
else:
    print('what a good name')