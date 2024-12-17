from random import randint
tickets = list()
run = list()
count = 0
how_many = int(input("how many tickets do you want? "))
while True:
    for c in range(0, 6):
        run.append(randint(1, 60))
    tickets.append(run[:])
    run.clear()
    count += 1
    if count == how_many:
        break
for e,t in enumerate(tickets):
    print(f"ticket {e+1}: {t}")
