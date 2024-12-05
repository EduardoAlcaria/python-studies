num = []
continue_answer = " "
while continue_answer not in "nN":
    num.append(int(input("Type a number: ")))
    continue_answer = str(input("Want to continues [y/n]: "))
print(f"You have typed {len(num)} numbers")
print(f"The numbers in descending order are {sorted(num, reverse=True)}")
if 5 in num:
    print("The number 5 is in the list")
else:
    print("The number 5 is not in the list")