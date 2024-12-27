age = 0
def needtovote(y):
    from datetime import datetime
    global age 
    age = datetime.today().year - y
    if age >= 16 and age < 18 or age > 65:
        return "OPTIONAL"
    if age >= 18 and age < 65:
        return "OBLIGATORY"
    else:
        return "DENNIED"
yearB = int(input("Year that you were born: "))
aVote = needtovote(yearB)
print(f"with {age} years old the vote right is {aVote}")