from time import sleep
print(f"{5 * '-='} FIREWORK CONTDOWN {5 * '-='}")
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print("BOOM")