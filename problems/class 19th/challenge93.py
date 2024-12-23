player_data = dict()
goals = list()
player_data['name'] = str(input("Name: "))
matches = int(input("How many matches does he played: "))
for m in range(0, matches):
    goals.append(int(input(f"how many goals on the {m} match? ")))
player_data['goals'] = goals[:]
player_data['total'] = sum(goals)
del goals
print("-="*30)
print(player_data)
print("-="*30)
for k, v in player_data.items():
    print(f"{k} has the value {v}")
print("-="*30)
print(f"The player {player_data['name']} played {len(player_data['goals'])} matches")
for e,v in enumerate(player_data['goals']):
    print(f"   => On match {e} he scored {v} goals")
print(f"it was a total of {player_data['total']} goals")