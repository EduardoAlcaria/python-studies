def player(name="", goals=0 ):
    if name == "":
        name = "<unknown>"
    if goals == "":
        goals = 0
    print(f"the player {name} did {goals} goal(s) at the tournament")
player_read = str(input("Player's name: "))
goals_read = str(input("how many goals: "))
player(player_read, goals_read)