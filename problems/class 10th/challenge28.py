from random import randint
n = randint(0, 5)
guess = int(input('Type a guess: '))
if guess == n:
    print('You won')
    print('The number was {}'.format(n))
else:
    print('You lost')
    print('The number was {}'.format(n))