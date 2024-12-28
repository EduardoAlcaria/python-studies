n = 1
odd = 0
even = 0
while n != 0:
    n = int(input("Enter a num "))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print(f"odd: {odd}, even {even}")