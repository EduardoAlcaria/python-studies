esp = str(input("Type a mathematics esprection: "))
p = []
for e in esp:
    if e == "(":
        p.append("(")
    elif e == ")":
        if len(p) > 0:
            p.pop()
        else:
            p.append(")")
            break
if len(p) == 0:
    print("Right")
else:
    print("Wrong")