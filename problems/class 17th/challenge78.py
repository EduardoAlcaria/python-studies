num = []
for v in range(0, 5):
    num.append(int(input(f"Type the value {v+1}: ")))
print(num)
print(f"the highest number is {max(num)}, and its position is {num.index(max(num))}")
print(f"the lower number is {min(num)}, and its position is {num.index(min(num))}")