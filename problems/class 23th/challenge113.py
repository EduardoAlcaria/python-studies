red = '\033[1;31m'
green = '\033[1;32m'
color_reset = '\033[m'
def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"{red}ERROR: invalid number, pleace type a valid integer number{color_reset}")
            continue
        except KeyboardInterrupt:
            print(f"\n{red}the integer numbers input has been stoped{color_reset}")
            return None
        else:
            return n
            break
def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f"{red}Invalid float number, place enter a valid float number{color_reset}")
            continue
        except KeyboardInterrupt:
            print(f"\n{red}the float numbers input has been stoped{color_reset}")
            return None
        else:
            return n
            break
numI = readint("Type an integer number: ")
numF = readfloat("Type a float value: ")
if numF == None and numI == None:
    print(f"{red}you havent typed any values{color_reset}")
elif numI == None:
    print(f"{red}you havent typed any integer number{color_reset}")
    print(f"{green}you have typed this float number: {numF}{color_reset}")
elif numF == None:
    print(f"{green}you have typed this integer number: {numI}{color_reset}")
    print(f"{red}you havent typed any float number{color_reset}")
else:
    print(f"{green}you have typed this integer number: {numI}{color_reset}")
    print(f"{green}you have typed this float number: {numF}{color_reset}")