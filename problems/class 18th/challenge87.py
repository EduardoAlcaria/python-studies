matrix = [[0,0,0], [0,0,0], [0,0,0]]
sEven = sColomn = 0
for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f"Type a number for the [{l}, {c}] position: "))
        if matrix[l][c] % 2 == 0:
            sEven += matrix[l][c]
        sColomn += matrix[l][2]
for m in matrix:
    print(f" [{m[0]:^5}] [{m[1]:^5}] [{m[2]:^5}]")
print(f"the sum between all the even numbers are {sEven}")
print(f"the highest number on the 2nd line is {max(matrix[1])}")
print(f"the sum of all numbers on the 3th colomn is {sColomn}")