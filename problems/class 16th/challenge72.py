number = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen", "twenty")
while True:
        ask_continue = " "
        while ask_continue not in "yn":
            verify_number = int(input("type a number between 0 and 20: "))
            if verify_number >= 0 and verify_number <= 20:
                print(f"you have typed the number {number[verify_number].upper()}")
                break
            else:
                print("pleace, ", end="")
        ask_continue = str(input("Do you want to continue [y/n]? ")).lower().strip()
        if ask_continue == "n":
             break
