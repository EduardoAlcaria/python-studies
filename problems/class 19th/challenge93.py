player = dict()
score = list()
score_sum = 0
player["name"] = str(input("Soccer player: "))
matches  = int(input("How many matches does he played? "))
for m in range(0, matches):
    score.append(int(input(f"match {m} How many points? ")))
    score_sum += score[m]
player["score"] = score[:]
player["score_sum"] = score_sum
score.clear()
print("-=" * 30)
print(player)
print("-=" * 30)
for i, v in player.items():
    print(f"The field {i} has the value {v}")
print("-=" * 30)
print(f"the player {player['name']} played {matches} matches")
for e,g in enumerate(player["score"]):
    print(f"     => At {e} match, he scored {g}")
print(f"The total score was {score_sum} goals")