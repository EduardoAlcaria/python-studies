from random import randint
tickets = list()
run = list()
how_many = int(input("how many tickets do you want? "))
tot = 1
while tot <= how_many:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in run:
            run.append(num)
            count += 1
        if count >= 6:
            break
    run.sort()
    tickets.append(run[:])
    run.clear()
    tot += 1
for e,t in enumerate(tickets):
    print(f"ticket {e+1} ---- {t}")


        