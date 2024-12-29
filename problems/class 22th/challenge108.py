from challenge108m import coin
num = float(input("Type the price: "))
print(f"the half part of {coin.coin(num)} is {coin.coin(coin.half(num))}")
print(f"the double part of {coin.coin(num)} is {coin.coin(coin.double(num))}")
print(f"increasing 10%, we have {coin.coin(coin.increase(num, 10))}")
print(f"decresing 13%, we have {coin.coin(coin.decrease(num, 13))}")