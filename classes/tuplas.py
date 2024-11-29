snacks = ("hamburger", "juice", "pizza", "candy")
for c in snacks:
    print(c)
for c in range(0, len(snacks)):
    print(snacks[c])
print("-="*30)
for enum,c in enumerate(snacks):
    print(f"{c}, {enum}")

