num = []
higher = 0
lower = 0
for c in range(0,5):
    num.append(int(input(f"Type a number [{c}/5]: ")))
    if c == 0:
        higher = num[c]
        lower = num[c]
    else:
        if num[c] > higher:
            higher = num[c]
        if num[c] < lower:
            lower = num[c]
print(f"you have typed this sequence {num}")
print(f"the higher value are {higher} and its position is: ",end="")
for e, h in enumerate(num):
    if h == higher:
        print(f"{e}...",end=" ")
print(f"\nand the lower value are {lower} and its position is: ",end="")
for e, l in enumerate(num):
    if l == lower:
        print(f"{e}...",end=" ")
print()