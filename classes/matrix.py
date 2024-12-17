galera = []
data = []
for c in range(0,3):
    data.append(str(input(f"name {c}: ")))
    data.append(int(input(f"idade {c}: ")))
    galera.append(data[:])
    data.clear()
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} e de maior")
    else:
        print(f"{p[0]} e de menor ")