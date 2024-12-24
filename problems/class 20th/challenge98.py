def count(b, e, s):
    print("-="*30)
    print(f"count down from {b} to {e} on {abs(s)} on {abs(s)}")
    for c in range(b, e+s, s):
        print(f"{c}",end=" ")
    print(f"\n{'-='*30}")
count(1, 10, 1)
count(10, 0, -2)
readB = int(input("Begin: "))
readE = int(input("End: "))
readS = int(input("Steps: "))
if readS == 0:
    readS = 1
if readS < 0:
     readS = abs(readS)
if readB > readE:
        count(readB, readE, -readS)
else:
     count(readB, readE, readS)
