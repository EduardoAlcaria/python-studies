n = int(input('Type an distance: '))
if n <= 200:
    print('you will pay {}$ for the bus ticket'.format(n * 0.50))
else:
    print('you will pay {}$ for the bus ticket'.format(n * 0.45))