player_data = dict()
score = list()
player_data['name'] = str(input("Soccer player name: "))
matches = int(input("How many matches does he played: "))
for m in range(matches):
    goal = int(input(f"How many goals did he score on {m} match: "))
    score.append(goal)
    player_data['goals'] = score[:]
    player_data['total'] = sum(score)
print("-=" * 30)
print(player_data)
print("-=" * 30)
for k, v in player_data.items():
    print(f"{k} has the value {v}")
print("-=" * 30)
print(f"the player {player_data['name']} has played {len(player_data['goals'])} matches")
for e,g in enumerate(score):
    print(f"      => On the {e} match he scored {g}")