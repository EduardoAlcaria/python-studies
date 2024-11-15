from random import randint
com_random = randint(0, 10)
player_guess = -1
trys = 1
while player_guess != com_random:
    player_guess = int(input("Enter yout guess [0-10]: "))
    if player_guess == com_random:
        print(f"you have won with {trys} trys")
    else:
        print("wrong try again")
        trys += 1

