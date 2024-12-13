numbers = list()
even = list()
odd = list()
for c in range(0, 7):
    n = int(input(f"Type a number:[{c+1}/7]: "))
    if n % 2 == 0:
        even.append(n)
    if n % 2 == 1:
        odd.append(n)
numbers.append(even[:])
even.clear()
numbers.append(odd[:])
odd.clear()
print(f"The even numbers are {sorted(numbers[0])}")
print(f"The odd numbers are {sorted(numbers[1])}")
