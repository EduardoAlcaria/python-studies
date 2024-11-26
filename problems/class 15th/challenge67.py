while True:
    n = int(input("Which multiplication table do you want to see: "))
    if n < 0:
        break
    for x in range(1,11):
        print(f"{n} x {x} = {n*x}")
print(f"End of the multiplication table program. Good Bye!")