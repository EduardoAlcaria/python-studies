num = []
even = []
odd = []
while True:
    num.append(int(input("Type a number: ")))
    continue_answer = str(input("Want to continue? [y/n]: ")).strip()
    if continue_answer in "nN":
        break
for v in range(len(num)):
    if num[v] % 2 == 0:
        even.append(num[v])
    if num[v] % 2 == 1:
        odd.append(num[v])
print(f"You have typed this sequence {sorted(num)}")
print(f"The odd numbers are {odd}")
print(f"And the even numbers are {even}")