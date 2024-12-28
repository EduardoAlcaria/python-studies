player_data = dict()
players = list()
goals = list()
while True:
    player_data.clear()
    goals.clear()
    player_data['name'] = str(input("Name: "))
    matches = int(input("How many matches does he played: "))
    for m in range(0, matches):
        goals.append(int(input(f"how many goals on the {m} match? ")))
    player_data['goals'] = goals[:]
    player_data['total'] = sum(goals)
    players.append(player_data.copy())
    while True:
        ask_continue = str(input("Continue? [y/n]: ")).strip()[0]
        if ask_continue in "nNYy":
            break
    if ask_continue in "nN":
        break
print("-=" * 30)
print(f"{'Code':<2} {'Name':<10} {'Goals':>3} {'Sum':>6}")
print("-"*60)
for e, p in enumerate(players):
    print(f"{e:<2}  {p['name']:<10} {str(p['goals']):>3} {p['total']:>6}")
while True:
    show_data = int(input("Show data from which player? (999 to stop): "))
    for e, n in enumerate(players):
        if show_data == e:
            print(f"----{n['name']}'s data")
            for e,v in enumerate(n['goals']):
                print(f"on the {e} match he scored {v} goals")
    if show_data > e and show_data != 999:
        print(f"there is no player with the {show_data} code, pleace try again")
    if show_data == 999:
        break
