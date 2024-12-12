num = []
higher = 0
lower = 0
for n in range(0,5):
    num.append(int(input(f"Type the {n+1}/5: ")))
    if n == 0:
        higher = num[n]
        lower = num[n]
    else:
        if num[n] > higher:
            higher = num[n]
        if num[n] < lower:
            lower = num[n]
print(f"the sequence is {sorted(num)}")
print(f"and higher value is {higher} and its position is: ",end="")
for e, h  in enumerate(num):
    if h == higher:
        print(f"{e}...",end=" ")
print(f"\nand the lower value is {lower} and its position is: ",end="")
for e, l in enumerate(num):
    if l == lower:
        print(f"{e}...",end=" ")
print()