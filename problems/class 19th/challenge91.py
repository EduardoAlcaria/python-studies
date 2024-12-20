from random import randint
from operator import itemgetter
sPlayer = list()
players = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6)}
for k,v in players.items():
    print(f"{k} got {v}")
sPlayer = sorted(players.items(), key=itemgetter(1), reverse=True)
print("==== RANKING ====")
for e, s in enumerate(sPlayer):
    print(f"    => {e+1} place: {s[0]} with {s[1]}")