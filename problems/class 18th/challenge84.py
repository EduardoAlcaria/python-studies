people = list()
data = list()
h = 0
l = 0
while True:
    data.append(str(input("Name: ")))
    data.append(float(input("KG: ")))
    if len(people) == 0:
        h = data[1]
        l = data[1]
    else:
        if data[1] > h:
            h = data[1]
        if data[1] < l:
            l = data[1]
    people.append(data[:])
    data.clear()
    ask_continue = str(input("Want to continue? [y/n]: ")).strip()
    if ask_continue in "nN":
        break
print(l)
print(f"you have typed {len(people)} peoples")
print(f"the lowest weight was {l} and it belongs to ", end="")
for p in people:
    if p[1] == l:
        print(f"[{p[0]}]",end=" ")
print(f"\nand the highest one was {h} and it belongs to ",end="")
for p in people:
    if p[1] == h:
        print(f"[{p[0]}]",end=" ")
print()
