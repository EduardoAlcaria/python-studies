peoples = []
data = {}
avarege_age = 0
while True:
    data["name"] = str(input("Name: "))
    while True:
        data["gen"] = str(input("Gen [m/f]: "))[0]
        if data["gen"] in "mfFM":
            break
        print("ERROR! Pleace type only M or F")
    data["age"] = int(input("Age: "))
    peoples.append(data.copy())
    data.clear()
    while True:
        ask_continue = str(input("Continue? [y/n]: "))[0]
        if ask_continue in "yYnN":
            break
        print("ERROR! Pleace type only Y or N")
    if ask_continue in "nN":
        break
for v in peoples:
    avarege_age += v['age']
avarege_age = avarege_age/len(peoples)
print(f"- You have typed {len(peoples)} peoples")
print(f"- The avarege age is {avarege_age:.2f}")
print(f"- The womans in the list are: ",end="")
for w in peoples:
    if w["gen"] in "fF":
        print(w["name"],end=" ")
print("\n- Peoples that are above the avarege age: ")
for p in peoples:
    if p["age"] >= avarege_age:
        print(f"   => name = {p['name']}; gen = {p['gen']}; age = {p['age']}")
print("<< END >>")
