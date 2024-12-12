esp = str(input("Type a mathematics esprection: "))
p = []
for c in esp:
    if c == "(":
        p.append("(")
    elif c == ")":
        if len(p) > 0:
            p.pop()
        else:
            p.append(")")
            break
if len(p) == 0:
    print("right")
else:
    print("wrong")