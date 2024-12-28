t = int(input("How many terms do you want? "))
fibo = 0
fibo2 = 1
aux = 1
for c in range(t):
    print(f"{fibo}",end=" -> ")
    fibo = aux
    aux = fibo2
    fibo2 += fibo
print("END")