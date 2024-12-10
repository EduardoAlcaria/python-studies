num = []
higher = 0
lower = 0
for c in range(0, 5):
    num.append(int(input(f"Type the [{c+1}/5] number: ")))
    if c == 0:
        higher = num[c]
        lower = num[c]
    else:
        if num[c] > higher:
            higher = num[c]
        if num[c] < lower:
            lower = num[c]
print(f"The sequence is {num}")
print(f"The lowest number is {lower} and its positon is: ",end="")
for e,l in enumerate(num):
    if l == lower:
        print(f"{e}... ",end="")
print(f"\nthe highest number is {higher} and its position is: ",end="")
for e, h in enumerate(num):
    if h == higher:
        print(f"{e}... ",end="")
print()