people_data = dict()
peoples = list()
avarage_age = 0
while True:
    people_data.clear()
    people_data['name'] = str(input("Name: "))
    while True:
        people_data['gen'] = str(input("Gen [M/F]: "))[0].strip()
        if people_data['gen'] in "mMfF":
            break
        else:
            print("ERROR! pleace type only M or F")
    people_data['age'] = int(input("Age: "))
    avarage_age += people_data['age']
    peoples.append(people_data.copy())
    while True:
        ask_continue = str(input("Continue? [Y/N]: "))[0].strip()
        if ask_continue in "nNYy":
            break
        else:
            print("ERROR! pleace type only Y or N")
    if ask_continue in "nN":
        break
print(f"A) You have registered {len(peoples)} peoples")
print(f"B) The avarage age is {avarage_age/len(peoples)}")
print(f"C) The womans in the list are ",end="")
for w in peoples:
    if w['gen'] in 'fF':
        print(w['name'],end=" ")
print()
print("D) Peoples that are above the avarege age: ")
for a in peoples:
    if a['age'] >= avarage_age/len(peoples):
        print(f"    name = {a['name']}; gen = {a['gen']}; age = {a['age']}")
print()