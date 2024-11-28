print("=" * 50)
withdraw = int(input("How much money do you want to withdraw: "))
total = withdraw
bill = 50
totbill = 0
while True:
    if total >= bill:
        total -= bill
        totbill += 1
    else:
        if totbill != 0:
            print(f"{totbill} bills of {bill}")
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totbill = 0
        if total == 0:
            break