def count(b, e, s):
    if s == 0:
        s = 1
    if s < 0:
        s = abs(s)
    print(f"{'-=' * 30}")
    print(f"count down from {b} to {e} on {abs(s)} on {abs(s)}")
    c = b
    if b < e:
        while c <= e:
            print(f"{c}",end=" ")
            c += s
    if b > e:
        while c >= e:
            print(f"{c}",end=" ")
            c -= s
    print("END")
    print(f"{'-='*30}")
count(1, 10, 1)
count(10, 0, -2)
readB = int(input("Begin: "))
readE = int(input("End: "))
readS = int(input("Steps: "))
count(readB, readE, readS)