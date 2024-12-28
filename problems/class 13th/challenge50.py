s = 0
count = 0
for c in range(1, 7):
    n = int(input(f"Type the {c} number: "))
    if n % 2 == 0:
        s += n
        count += 1
print(f"you have typed {count} even numbers and the summing is {s}")