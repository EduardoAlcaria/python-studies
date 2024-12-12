num = []
while True:
    n = int(input("Type a number: "))
    if n not in num:
        num.append(n)
        print("number add")
    else:
        print("this number was already add")
    continue_answer = str(input("Do you want to continue? [y/n]: ")).strip()
    if continue_answer in "nN":
        break
print(f"you have typed this sequence {sorted(num)}")