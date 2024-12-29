from challenge107m import coin
num = float(input("Type the price: $"))
print(f"the half part of {num} is ${coin.half(num)}")
print(f"the double part of {num} is ${coin.double(num)}")
print(f"increasing 10%, we have ${coin.increase(num, 10):.2f}")
print(f"decresing 13%, we have ${coin.decrease(num, 13)}")