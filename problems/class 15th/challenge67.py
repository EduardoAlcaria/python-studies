while True:
    n = int(input("Which multiplication table do you want to see: "))
    print("_"*10)
    if n < 0:
        break
    for x in range(1,11):
        print(f"{n} x {x} = {n*x}")
    print("_"*60)
print(f"End of the multiplication table program. Good Bye!")