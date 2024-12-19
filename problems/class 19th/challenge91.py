from datetime import datetime
person = dict()
person["name"] = str(input("Name: "))
person["age"] = int(input("Born year: "))
person["ctps"] = int(input("Work license (type 0 if you dont have): "))
if person["ctps"] != 0:
    person["hireY"] = int(input("Hire year: "))
    person["retirement"] = person["hireY"] - person["age"] + 35
    person["salary"] = float(input("Salary: "))
person["age"] = datetime.today().year - person["age"]
print("-=" * 30)
for p, v in person.items():
    print(f"{p} has the value {v}")