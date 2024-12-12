num = []
while True:
    num.append(int(input("Type a number: ")))
    continue_answer = str(input("Want to continue? [y/n]: ")).strip()
    if continue_answer in "nN":
        break
print(f"you have typed this sequence {sorted(num,reverse=True)}")
print(f"and it has {len(num)+1} elements")
if 5 in num:
    print(f"The number 5 is in the list")
else:
    print("the number 5 is not in the list")