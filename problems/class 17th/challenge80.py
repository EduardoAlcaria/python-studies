num = []
for c in range(0, 5):
    n = int(input("Type a number: "))
    if c == 0 or n > num[-1]:
        num.append(n)
        print("add into the last position")
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f"add into the {pos}")
                break
            pos += 1
print(num)