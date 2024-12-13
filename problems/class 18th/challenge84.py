people = list()
data = list()
highW = 0
lowW = 0
while True:
    data.append(str(input("Name: ")))
    data.append(int(input("Weight: ")))
    people.append(data[:])
    data.clear()
    continue_asnwer = str(input("want to continue? [y/n]: ")).strip()
    if continue_asnwer in "nN":
        break
for e, w in enumerate(people):
    if e == 0:
        highW = w[1]
        lowW = w[1]
    else:
        if w[1] > highW:
            highW = w[1]
        if w[1] < lowW:
            lowW = w[1]
print(f"you have typed {len(people[0])} peoples")
print(f"The lowest weight was {lowW} and it belongs to ",end="")
for e, l in enumerate(people):
    if lowW == l[1]:
        print(f"[{people[e][0]}]",end=" ")
print(f"\nthe highest weight was {highW} and it belongs to ",end="")
for e, h in enumerate(people):
    if highW == h[1]:
        print(f"[{people[e][0]}]",end=" ")
print()
