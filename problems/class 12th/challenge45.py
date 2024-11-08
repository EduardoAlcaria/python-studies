from random import randint
green = "\033[1;32m"
red = "\033[1;31m"
reset = "\033[0m"

itens = ('rock', 'paper', 'scissors')
pc = randint(0, 2)

play = int(input("""what do you want to throw
[0] rock
[1] paper
[2] scissors
> """))

if play not in [0, 1, 2]:
    print('invalid choice')
else:
    print('you threw {}'.format(itens[play]))
    print('the COM threw {}'.format(itens[pc]))

    #tie
    if itens[play] == itens[pc]:
        print('\033[1;33mits a tie\033[0m')
    #won
    elif itens[play] == 'paper' and itens[pc] == 'rock':
        print(green ,'You Won', reset)
    elif itens[play] == 'scissors' and itens[pc] == 'paper':
        print(green ,'You Won', reset)
    elif itens[play] == 'rock' and itens[pc] == 'scissors':
        print(green, 'you Won', reset)
    #lost
    else:
        print(red, 'You Lost', reset)
