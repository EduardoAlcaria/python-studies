l1 = []
l2 = []
l3 = []
sumC = 0
sumE = 0
matrix = []
for c in range(0, 3):
    l1.append(int(input(f"type a num to [0,{c}]: ")))
for c in range(0, 3):
    l2.append(int(input(f"type a num to [1,{c}]: ")))
for c in range(0, 3):
    l3.append(int(input(f"type a num to [2,{c}]: ")))
matrix.append(l1[:])
matrix.append(l2[:])
matrix.append(l3[:])
for m in matrix:
    print(f"[ {m[0]} ] [ {m[1]} ] [ {m[2]} ]")
for m in matrix:
    sumC += m[2]
    if m[0] % 2 == 0:
        sumE += m[0]
    if m[1] % 2 == 0:
        sumE += m[1]
    if m[2] % 2 == 0:
        sumE += m[2]
print(f"the sum from the 3th coloum numbers are {sumC}") 
print(f"the highest coloum 2nd number is {max(l2)}")
print(f"the sum of all even numbers are {sumE}")