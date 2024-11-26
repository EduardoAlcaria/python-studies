n = 0
s = 0
while True:
    n = int(input("Type a number [type 999 to stop]: "))
    if n == 999:
        break
    s += n
print(f"the sum is {s}")
