num = []
continue_answer = " "
while True:
    n = int(input("Type a number: "))
    if n not in num:
        num.append(n)
        print("number add")
    else:
        print("number already add")
    continue_answer = str(input("want to continue? [y/n] ")).strip()
    if continue_answer in "nN":
        break
print(sorted(num))
