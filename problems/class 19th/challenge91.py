from random import randint
from operator import itemgetter
players = {"Player1": randint(1, 6),
           "Player2": randint(1, 6),
           "Player3": randint(1, 6),
           "player4": randint(1, 6)}
for k, v in players.items():
    print(f"the player {k} got {v}")
print("======= RANKING =======")
sorted_players = sorted(players.items(), key=itemgetter(1), reverse=True)
for e, v in enumerate(sorted_players):
    print(f"{e+1} Place: {v[0]}")