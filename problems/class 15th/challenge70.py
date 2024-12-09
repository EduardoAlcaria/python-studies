tot_purchase = 0
more_thousand = 0
cheaper_price = 0
count = 0
cheaper_name = " "
while True:
    product_name = str(input("Product name: "))
    price = float(input("Price: $"))
    count += 1
    if count == 1 or price < cheaper_price:
        cheaper_name = product_name
        cheaper_price = price
    if price > 1000:
        more_thousand += 1
    tot_purchase += price
    continue_answer = " "
    while continue_answer not in "yn":
        continue_answer = str(input("Do you want to continue [y/n]? ")).lower().strip()[0]
    if continue_answer == "n":
        break
print("{:-^40}".format("Purchase Analysis"))
print(f"Purchase total ${tot_purchase:.2f}")
print(f"There is {more_thousand} product that cost more than $1000")
print(f"The cheaper item is {cheaper_name.capitalize()} and it costs ${cheaper_price:.2f}")