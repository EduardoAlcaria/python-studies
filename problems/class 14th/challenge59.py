from time import sleep
choice = ""
n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))
while choice != "5":
    print(20*"-=", end="\n")
    if choice == "4":
        n1 = float(input("Enter a new number: "))
        n2 = float(input("Enter a another new number: "))
    choice = str(input("""
Addiction [1]
Subtraction [2]
major number [3]
new numbers [4]
Exit [5]                      
> """))
    if choice == "1":
        print(f"the sum is {n1 + n2}")
        sleep(1)
    elif choice == "2":
        print(f"the difference is {n1 - n2}")
        sleep(1)
    elif choice == "3":
        if n1 > n2:
            print(f"The major number is {n1}")
            sleep(1)
        elif n2 > n1:
            print(f"the major number is {n2}")
            sleep(1)
        else:
            print(f"They are the same")
            sleep(1)
    elif choice == "5":
        print("exiting")
    else:
        print("invalid option try again")
    