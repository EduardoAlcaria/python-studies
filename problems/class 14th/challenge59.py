again = ""
choice = ""
while not choice == "5" and not again == "n":
    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter another number: "))
    choice = str(input("""
Addiction [1]
Subtraction [2]
major number [3]
new numbers [4]
Exit [5]                      
> """))
    if choice == "1":
        print(f"the sum is {n1 + n2}")
        again = str(input("You want to try again? [y/n]: ")).lower()
    elif choice == "2":
        print(f"the difference is {n1 - n2}")
        again = str(input("You want to try again? [y/n]: ")).lower()
    elif choice == "3":
        if n1 > n2:
            print(f"The major number is {n1}")
        elif n2 > n1:
            print(f"the major number is {n2}")
        else:
            print(f"They are the same")
        again = str(input("You want to try again? [y/n]: "))
    elif choice == "4": 
        print("type new numbers")
print("exiting")
    