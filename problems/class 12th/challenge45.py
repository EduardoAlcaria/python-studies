from random import choice

rpc_list = ["rock", "paper", "scissors"]
pc = choice(rpc_list)

play = str(input('what do you want to trow > '))
#tie
if play == pc:
    print('its a tie')
#COM
elif play == 'rock' and pc == 'paper':
    print('the COM has won')
    print('the COM trew {}'.format(pc))
elif play == 'paper' and pc == 'scissors':
    print('the COM has won')
    print('the COM trew {}'.format(pc))
elif play == 'scissors' and pc == 'rock':
    print('the COM has won')
    print('the COM trew'.format(pc))
#player
elif play == 'paper' and pc == 'rock':
    print('you have won')
    print('the COM trew {}'.format(pc))
elif play == 'scissors' and pc == 'paper':
    print('you have won')
    print('the COM trew {}'.format(pc))
elif play == 'rock' and pc == 'scissors':
    print('you have won')
    print('the COM trew {}'.format(pc))
else:
    print('you have typed something wrong')
