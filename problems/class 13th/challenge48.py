s = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(f"The sum of all odd numbers between 1 and 500 is {s}")

