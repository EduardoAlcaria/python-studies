n = 0
s = 0
c = 0
while n != 999:
    n = int(input("Type a number [type 999 to stop]: "))
    c += 1
    s += n
print(f"you have typed {c-1} values and the sum between them are {s - 999}")
