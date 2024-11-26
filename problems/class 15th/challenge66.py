n = 0
s = 0
count = 0
while True:
    n = int(input("Type a number [type 999 to stop]: "))
    if n == 999:
        break
    s += n
    count += 1
print(f"you have typed {count} numbers and the sum is {s}")
