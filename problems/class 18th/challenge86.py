l1 = []
l2 = []
l3 = []
matrix = []
for c in range(0, 3):
    l1.append(int(input(f"type a num to [0,{c}]: ")))
for c in range(0, 3):
    l2.append(int(input(f"type a num to [1,{c}]: ")))
for c in range(0, 3):
    l3.append(int(input(f"type a num to [2,{c}]: ")))
matrix.append(l1[:])
l1.clear()
matrix.append(l2[:])
l2.clear()
matrix.append(l3[:])
l3.clear()
for m in matrix:
    print(f"[ {m[0]} ] [ {m[1]} ] [ {m[2]} ]")