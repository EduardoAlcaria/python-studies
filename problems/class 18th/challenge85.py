num = []
even = list()
odd = list()
for c in range(0, 7):
    n = int(input(f"Type the {c+1} number: "))
    if n % 2 == 1:     
        even.append(n)
    if n % 2 == 0:
        odd.append(n)
num.append(odd[:])
num.append(even[:])
even.clear()
odd.clear()
print(f"the even values are {sorted(num[0])}")
print(f"the odd values are {sorted(num[1])}")
