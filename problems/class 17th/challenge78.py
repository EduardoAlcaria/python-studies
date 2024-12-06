num = []
higher = 0
lower = 0
for c in range(0,5):
    num.append(int(input(f"Type the {c+1} number: ")))
    if c == 0:
        higher = num[c]
        lower = num[c]
    else:
        if num[c] > higher:
            higher = num[c]
        if num[c] < lower:
            lower = num[c]
print(f"the sequence is {num}")
print(f"the highest number is {higher} and its position is ", end="")
for i, c in enumerate(num):
    if c == higher:
        print(f"{i}... ",end="")
print(f"\nthe lowest number is {lower} and its position is ",end="")
for i, c in enumerate(num):
    if c == lower:
        print(f"{i}... ", end="")
print()