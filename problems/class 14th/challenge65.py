again = ""
n = 0
s = 0
count = 0
major = 0
minor = 0
while again != "n":
    n = int(input("Type a number: "))
    again = str(input("Do you want to type another one? [S/N] ")).lower().strip()[0]
    s += n
    count += 1
    if count == 1:
        major = n
        minor = n
    else:
        if n > major:
            major = n
        if n < minor:
            minor = n
print(f"\nYou have typed {count} values and the avarege are {s/count:.2f}")
print(f"the major value are {major}, and the minor one is {minor}")
