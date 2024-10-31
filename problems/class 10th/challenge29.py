km = float(input('Type a speed KM: '))
if km > 80:
    print('You have been fined on {:.2f}$'.format((km - 80) * 7)) 
else:
    print('Have a good day, drive safety!')