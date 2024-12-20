from random import randint
from operator import itemgetter
players = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6)}
sorted_players = dict()
for k,v in players.items():
    print(f"{k} got {v}")
print("-=" * 30)
print("=== RANKING ===")
sorted_players = sorted(players.items(), key=itemgetter(1), reverse=True)
for e, p in enumerate(sorted_players):
    print(f"{e+1} place: {p[0]} got {p[1]}")