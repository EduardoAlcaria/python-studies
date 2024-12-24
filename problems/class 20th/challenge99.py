def major(* num):
    print("-=" * 30)
    for v in num:
        print(f"{v}",end=" ")
    print(f"you have typed {len(num)} values")
    print(f"the higher value was {max(num)}")
    print("-=" * 30)
major(2, 9, 4, 5, 7, 1)
major(4, 7, 0)
major(0)