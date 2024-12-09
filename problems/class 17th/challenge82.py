num = []
even = []
odd = []
continue_answer = " "
while continue_answer not in "nN":
    num.append(int(input("Type a number: ")))
    continue_answer = str(input("Want to continue? [y/n] ")).strip()
for c in range(0, len(num)):
    if num[c] % 2 == 0:
        even.append(num[c])
    if num[c] % 2 == 1:
        odd.append(num[c])
print(f"the complete list are {num}")
print(f"the list of even numbers are {even}")
print(f"the list of odd numbers are {odd}")