num = []
continue_question = " "
c = 0
while continue_question not in "nN":
    num.append(int(input("Type a number: ")))
    if num.count(num[c]) > 1:
        print("number already added")
        del(num[c])
    else:
        print("Number added")
        c += 1
    continue_question = str(input("Want to continue? [y/n] ")).strip()
print(sorted(num))
