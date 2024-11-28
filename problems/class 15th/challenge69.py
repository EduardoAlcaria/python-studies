gen = " "
majorage = 0
totmale = 0
fem_less_20 = 0
while True:
    age = int(input("Age: "))
    gen = str(input("Gender: [M/F]: ")).lower().strip()
    while gen not in "mf":
        gen = str(input("Gender: [M/F]: ")).lower().strip()
    if age > 18:
        majorage += 1
    if gen == "m":
        totmale += 1
    else:
        if gen == "f" and age < 20:
            fem_less_20 += 1
    answer = str(input("Would you like to continue: [y/n]: ")).lower().strip()
    if answer == "n":
        break
print(f"There is {majorage} peoples above 18 years old")
print(f"There is {totmale} males")
print(f"There are {fem_less_20} under 20 years old")
