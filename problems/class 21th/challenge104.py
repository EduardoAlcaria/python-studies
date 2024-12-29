def readint(msg):
    num = str(input(msg))
    if num.isnumeric():
        num = int(num)
        return num
    else:
        while True:
            print("\033[1;31mERROR pleace type a integer number: \033[m")
            num = input("type a number: ")
            if num.isnumeric():
                break
        num = int(num)
        return num
n = readint("type a number: ")
print(f"you have typed {n}")