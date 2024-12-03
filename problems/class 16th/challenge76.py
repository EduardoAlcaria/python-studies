products = ("pen", 3,
            "notebook", 2000, 
            "apple", 4)
print("_"*45)
print("{:^35}".format("PRODUCT LIST"))
print("_"*45)
for c in range(0, len(products), 2):
    print("{:.<30}".format(products[c]), end="")
    print(f"${products[c+1]:.2f}")
print("_"*45)
