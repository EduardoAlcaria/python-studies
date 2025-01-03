matrix = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f"Type a number for [{l}, {c}] position: "))
for m in matrix:
    print(f"[ {m[0]:^5} ] [ {m[1]:^5} ] [ {m[2]:^5} ]")