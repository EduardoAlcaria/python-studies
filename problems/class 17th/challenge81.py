num = []
while True:
    num.append(int(input("Type a number: ")))
    continue_answer = str(input("Want to continue? [y/n]: ")).strip()
    if continue_answer in "nN":
        break
print(f"you hae typed this sequence {sorted(num,reverse=True)}")
print(f"you have typed {len(num)} elements")
if 5 in num:
    print("the number 5 is in the list")
else:
    print("the number 5 is not in the list")