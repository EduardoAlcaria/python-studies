players = []
goals = []
data = {}
while True:
    data["name"] = str(input("Name: "))
    data["matches"] = int(input("How many matches does he played? "))
    sum_goals = 0
    for m in range(0, data['matches']):
        g = int(input(f"Match {m} goals: "))
        sum_goals += g
        goals.append(g)
    data["sum_goal"] = sum_goals
    data["goals"] = goals[:]
    players.append(data.copy())
    data.clear()
    goals.clear()
    ask_continue = str(input("Continue? [y/n]: ")).strip()
    if ask_continue in "nN":
        break
print("-=" * 30)
print(f"{'Code':<2} {'Name':<10} {'Goals':>4} {'Sum':>4}")
print("-"*60)
for e, p in enumerate(players):
    print(f"{e:<2}  {p['name']:<10} {p['goals']} {p['sum_goal']:>4}")
while True:
    choise = int(input("Show data from which player? [999 to stop]: "))
    for i, p in enumerate(players):
        if choise == i:
            print(f"---{p['name']}`s data: ")
            for e, g in enumerate(players[i]['goals']):
                print(f"  On match {e} he did {g} goals")
    if choise > len(players):
        print(f"ERROR! There's no player with the code {choise} place try again")
    if choise == 999:
        break
      
            