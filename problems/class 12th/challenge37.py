n = int(input('Enter a number: '))
choice = str(input('You want to conver the number into:\n [1] binary  [2] octal  [3] hexadecimal '))
if choice == '1':
    print('the binary is {}'.format(bin(n)[2:]))
elif choice == '2':
    print('The octal is {}'.format(oct(n)[2:]))
elif choice == '3':
    print('The hex is {}'.format(hex(n)[2:]))
else:
    print('bye')