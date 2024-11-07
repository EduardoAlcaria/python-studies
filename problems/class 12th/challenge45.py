from random import choice

rpc_list = ["rock", "paper", "scissors"]
pc = choice(rpc_list)

green = "\033[1;32m"
red = "\033[1;31m"
reset = "\033[0m"

play = str(input('what do you want to trow > '))
#tie
if play == pc:
    print('\033[1;33mits a tie\033[0m')
#COM
elif play == 'rock' and pc == 'paper':
    print('{} the COM has won {}'.format(red, reset))
    print('the COM trew {}'.format(pc))
elif play == 'paper' and pc == 'scissors':
    print('{} the COM has won {}'.format(red, reset))
    print('the COM trew {}'.format(pc))
elif play == 'scissors' and pc == 'rock':
    print('{} the COM has won {}'.format(red, reset))
    print('the COM trew'.format(pc))
#player
elif play == 'paper' and pc == 'rock':
    print('{} you have won {}'.format(green, reset))
    print('the COM trew {}'.format(pc))
elif play == 'scissors' and pc == 'paper':
    print('{} you have won {}'.format(green, reset))
    print('the COM trew {}'.format(pc))
elif play == 'rock' and pc == 'scissors':
    print('{} you have won {}'.format(green, reset))
    print('the COM trew {}'.format(pc))
else:
    print('you have typed something wrong')
