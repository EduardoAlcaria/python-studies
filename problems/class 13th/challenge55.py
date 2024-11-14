minW = 0
maxW = 0
for c in range(1, 6):
    p = float(input(f"Weight of the {c} person: "))
    if c == 1:
        minW = p
        maxW = p
    else:
        if p > maxW:
            maxW = p
        elif p < minW:
            minW = p
print(maxW)
print(minW)