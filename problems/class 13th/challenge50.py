s = 0
for c in range(1, 7):
    n = int(input(f"Type the {c} number: "))
    if n % 2 == 0:
        s += n
print(f"the summing is {s}")