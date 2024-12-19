state = dict()
brazil = list()
for c in range(0,3):
    state["uf"] = str(input("State: "))
    state["acronym"] = str(input("Acronym: "))
    brazil.append(state.copy())
for s in brazil:
    for v in s.values():
        print(v, end=" ")
    print()