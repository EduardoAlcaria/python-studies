peoples = list()
data = list()
totabove = totunder = 0
for c in range(0, 3):
    data.append(str(input("Name: ")))
    data.append(int(input("Age: ")))
    peoples.append(data[:])
    data.clear()
for p in peoples:
    if p[1] >= 21:
        print(f"{p[0]} is above 21")
        totabove += 1
    else:
        print(f"{p[0]} is under 21")
        totunder += 1
print(f"there is {totabove} peoples above 21\nand {totunder} peoples under 21")