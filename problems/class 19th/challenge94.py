peoples = []
data = {}
avarege_age = 0
while True:
    data["name"] = str(input("Name: "))
    data["age"] = int(input("Age: "))
    data["gen"] = str(input("Gen [m/f]: "))
    peoples.append(data.copy())
    data.clear()
    ask_continue = str(input("Continue? [y/n]: ")).strip()
    if ask_continue in "nN":
        break
for v in peoples:
    avarege_age += v['age']
avarege_age = avarege_age/len(peoples)
print("-=" * 30)
print(f"- You have typed {len(peoples)} peoples")
print(f"- The avarege age is {avarege_age:.2f}")
print(f"- The womans in the list are: ",end="")
for w in peoples:
    if w["gen"] == "f":
        print(w["name"],end=" ")
print("\n- Peoples that are above the avarege age: ")
for p in peoples:
    if p["age"] > avarege_age:
        print(f"name = {p['name']}; gen = {p['gen']}; age = {p['age']}")
print("<< END >>")
