from datetime import datetime
def needtovote(y):
    global age
    if age < 18:
        return "DENIED"
    if age >= 18 and age < 65:
        return "OBLIGATORY"
    else:
        return "OPTIONAL"
yearB = int(input("Year that you were born: "))
age = datetime.today().year - yearB
aVote = needtovote(yearB)
print(f"with {age} the vote right is {aVote}")