def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERROR type a valid integer number\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[1;31mthe integer input has been stoped\033[m")
            break
        else:
            return n
def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERROR type a valid float number\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[1;31mthe float input has been stoped\033[m")
            break
        else:
            return n
numI = readint("type a integer number: ")
numF = readfloat("type a float number: ")
if numI == None and numF == None:
    print("you havent type any numbers")    
elif numF == None:
    print(f"you have typed the integer number {numI}")
    print(f"you havent typed a float number")
elif numI == None:
    print(f"you havent type an integer number")
    print(f"you have typed the float number {numF}")
else:
    print(f"you have typed the integer number {numI}")
    print(f"you have typed the float number {numF}")