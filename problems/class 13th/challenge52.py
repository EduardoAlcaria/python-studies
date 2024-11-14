count = 0
n = int(input("Type a number: "))
for c in range(1, n+1):
    if n % c == 0:
        print("\033[032m",c,"\033[m", end=" ")
        count += 1
    else:
        print("\033[031m",c,"\033[m", end=" ")
if  count == 2:       
    print(f"\n \033[1;32mIts a prime number\033[m")
else:
    print(f"\n \033[1;31mIts not a prime number\033[m")