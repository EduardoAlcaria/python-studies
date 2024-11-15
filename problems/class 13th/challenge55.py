minW = 0
maxW = 0
for c in range(1,6):
    w = float(input(f"Weight of the {c} person: "))
    if c == 1:
        minW = w
        maxW = w
    else:
        if w > maxW:
            maxW = w
        if w < minW:
            minW = w
print(f"the minimal weight was {minW}KG")
print(f"the max weight was {maxW}KG")