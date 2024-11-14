s = 0
count = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        count += 1
print(f"The sum of all {count} odd numbers between 1 and 500 is {s}")

