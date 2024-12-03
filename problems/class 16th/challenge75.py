evenN = 0
nums = (int(input("Typa a number: ")),
        int(input("Typa another number: ")),
         int(input("Typa more one number: ")), 
         int(input("Typa the last number: ")))
for c in nums:
    if c % 2 == 0:
        evenN += c
print(f"You have typed {nums}")
print(f"The number 9 has appeared in {nums.count(9)} times")
if 3 in nums:
    print(f"The number 3 has appeared in {nums.index(3)+1} position")
else:
    print(f"the number 3 has not appeared in any positon")
print(f"The sum of the even numbers is {evenN}")