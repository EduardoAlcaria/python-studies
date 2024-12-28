from random import randint
ran = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("the random values are: ", end="")
less = 0
more = 0
for c in range(0, len(ran)):
    print(f"{ran[c]} ", end="")
    if c == 0:
        more = ran[c+1]
        less = ran[c]
    else:
        if more < less:
            less = more
        else:
            if less > more:
                more = less
print(f"\nthe lowest random number is {less}")
print(f"the highest random number is {more}")
            