n1 = float(input('Type a measure: '))
n2 = float(input('Type a measure: '))
n3 = float(input('Type a measure: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('it can be a triangule')
else:
    print('it can not be a triangule')
    