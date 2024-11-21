f = int(input("Enter the first term: "))
r = int(input("Enter the reason: "))
term = r
c = 1
more = 1
tot = 10
while more != 0:
    while c < tot:
        print(f"{term}",end=" -> ")
        term += r
        c += 1
    print("Pause")
    more = int(input("How many terms do you want more? "))
    tot += more
print(f"All progressions has been showed, with {tot} terms")