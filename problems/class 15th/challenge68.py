from random import randint
win = 0
while True:
    com_play = randint(0, 10)
    player_play = int(input("Type a value: "))
    total = player_play + com_play
    even_odd = " "
    while even_odd not in "eo":
        even_odd = str(input("Even or odd [E/O]? ")).lower().strip()[0]
    if total % 2 == 0 and even_odd == "e":
            win += 1
            print("You have won")
            print(f"you played {player_play} and the computer played {com_play}, {total} is EVEN")
            print("lets play again")
    elif total % 3 == 0 and even_odd == "o":
            win += 1
            print("You have won")
            print(f"you played {player_play} and the computer played {com_play}, {total} is ODD")
            print("lets play again")
    else:
        print("you have lost")
        if even_odd == "o":
            print(f"you played {player_play} and the computer played {com_play}, {total} is EVEN")
        else:
           print(f"you played {player_play} and the computer played {com_play}, {total} is ODD")  
        break
print(f"you have won {win} times")