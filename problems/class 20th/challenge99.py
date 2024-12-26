def major(* num):
    h = 0
    for e, c in enumerate(num):
        if e == 0:
            h = c
        else:
            if c > h:
                h = c
    print("-=" * 30)
    for v in num:
        print(f"{v}",end=" ")
    print(f"you have typed {len(num)} values")
    print(f"the higher value was {h}")
major(2, 9, 4, 5, 7, 1)
major(4, 7, 0)
major(0)