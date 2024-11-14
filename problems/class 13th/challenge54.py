from datetime import datetime
cyear = datetime.now().year
major = 0
minor = 0
for c in range(1, 8):
    year = int(input(f"which year the {c} person was born: "))
    if cyear - year >= 18:
        major += 1
    else:
        minor += 1
print(f"there are {major} people on major age")
print(f"and there are {minor} people on minor age")