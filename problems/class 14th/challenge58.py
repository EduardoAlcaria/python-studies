from random import randint
com_random = randint(0, 10)
player_guess = -1
trys = 1
while player_guess != com_random:
    player_guess = int(input("Enter your guess [0-10]: "))
    if player_guess == com_random:
        print(f"you have won with {trys} trys")
    elif player_guess > com_random or player_guess < com_random:
        if player_guess == 10 or player_guess > com_random:
            print("Try a lower number")
            trys += 1
        else:
            print("Try a higher number")
            trys += 1
    

