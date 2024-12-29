from challenge109m import coin
num = float(input("Type the price: "))
print(f"the half part of {coin.coin(num)} is {coin.half(num, True)}")
print(f"the double part of {coin.coin(num)} is {coin.double(num, True)}")
print(f"increasing 10%, we have {coin.increase(num, 10, True)}")
print(f"decresing 13%, we have {coin.decrease(num, 13, True)}")