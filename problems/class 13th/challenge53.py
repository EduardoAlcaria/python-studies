f = str(input("Type a sentence: ")).lower().replace(" ", "").strip()
for c in range(len(f), 0, - 1):
    print(f[c-len(f)-1],end="")


