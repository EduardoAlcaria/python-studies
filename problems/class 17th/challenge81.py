num = []
continue_answer = " "
while continue_answer not in "nN":
    num.append(int(input("The a number: ")))
    continue_answer = str(input("Want to continue? [y/n]")).strip()
print(f"you have typed {len(num)}")
print(f"the descending or of them is {sorted(num,reverse=True)}")
if 5 in num:
    print("the number 5 is in the list")
else:
    print("the number 5 is not in the list")