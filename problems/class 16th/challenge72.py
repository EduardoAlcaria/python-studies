number = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen", "twenty")
while True:
    verify_number = int(input("type a number between 0 and 20: "))
    if verify_number >= 0 and verify_number <= 20:
        print(number[verify_number])
        break
    else: 
        print("pleace, ", end="")
        
