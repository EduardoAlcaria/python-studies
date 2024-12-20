player_data = dict()
score = list()
tot = 0
player_data['name'] = str(input("Soccer player name: "))
matches = int(input("How many matches does he played: "))
for m in range(matches):
    goal = int(input(f"How many goals did he score on {m} match: "))
    tot += goal
    score.append(goal)
    player_data['goals'] = score[:]
    player_data['total'] = tot
print("-=" * 30)
for k, v in player_data.items():
    print(f"{k} has the value {v}")
print("-=" * 30)
print(f"the player {player_data['name']} has played {matches} matches")
for e,g in enumerate(score):
    print(f"      => On the {e} match he scored {g}")