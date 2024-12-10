num = []
while True:
    n = int(input("Type a number: "))
    if n not in num:
        print("number add")
        num.append(n)
    else:
        print("number already add, pleace enter another one")
    continue_answer = str(input("would like to enter another one? [y/n]: ")).strip()
    if continue_answer in "nN":
            break
print(f"You have typed this numbers {sorted(num)}")
if 5 in num:
    print("The number 5 are among them")
else:
    print("the number 5 is arent among them ")