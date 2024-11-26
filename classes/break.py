n = 0
s = 0
while True:
    n = int(input("type a number: "))
    if n == 999:
        break
    s += n
print(f"The sum is {s}")