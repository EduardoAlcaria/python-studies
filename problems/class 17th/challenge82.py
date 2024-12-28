num = []
even = []
odd = []
while True:
    num.append(int(input("Type a number: ")))
    continue_asnwer = str(input("want to continue? [y/n]: ")).strip()
    if continue_asnwer in "nN":
        break
for v in num:
    if v % 2 == 0:
        even.append(v)
    if v % 2 == 1:
        odd.append(v)
print(f"{sorted(v)}")
print(f"{even}")
print(f"{odd}")