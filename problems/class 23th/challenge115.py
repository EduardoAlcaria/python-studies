from challenge115pkg import menu, base, line
while True:
    r = menu(["Show registered peoples", "register new people", "exit"])
    if r == 1:
        base.createfile(r)
        line("PEOPLE's LIST")
        base.readfile()
    elif r == 2:
        name = str(input("Type the name: "))
        age = int(input("Type the age: "))
        ret = base.writefile(name, age)
        print(ret)
    else:
        break