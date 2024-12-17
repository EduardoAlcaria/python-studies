people = list()
data = list()
h = 0
l = 0
while True:
    data.append(str(input("Name: ")))
    data.append(int(input("KG: ")))
    people.append(data[:])
    data.clear()
    ask_continue = str(input("Want to continue? [y/n]: ")).strip()
    if ask_continue in "nN":
        break
for e,p in enumerate(people):
    if e == 0:
        h = p[1]
        l = p[1]
    else:
        if p[1] > h:
            h = p[1]
        if p[1] < l:
            l = p[1]
print(f"the lowest weight was {l} and it belongs to ", end="")
for p in people:
    if p[1] == l:
        print(p[0],end=" ")
print(f"\nand the highest one was {h} and it belongs to ",end="")
for p in people:
    if p[1] == h:
        print(p[0],end=" ")
print()
