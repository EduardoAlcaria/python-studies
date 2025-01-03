num = [[], []]
for c in range(1, 8):
    n = int(input(f"Type the {c}/7 number: "))
    if n % 2 == 0:     
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
print(f"the even values are {sorted(num[0])}")
print(f"the odd values are {sorted(num[1])}")
