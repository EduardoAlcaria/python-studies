num = []
while True:
    n = int(input("Type a number: "))
    if n not in num:
        num.append(n)
        print(f"number {n} added")
    else:
        print(f"the number {n} was already added")
    continue_answer = str(input("Want to continue? [y/n]: ")).strip()
    if continue_answer in "nN":
        break
print(f"you have typed this sequence {sorted(num)}")