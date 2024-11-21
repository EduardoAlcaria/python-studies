f = int(input("First term: "))
r = int(input("Reason: "))
term = f
c = 1
while c <= 10:
    print(f"{term}",end=" -> ")
    term += r
    c += 1
print("END")