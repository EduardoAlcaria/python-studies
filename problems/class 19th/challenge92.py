from datetime import datetime
worker = dict()
worker['name']  = str(input("Name: "))
born = int(input("Born year: "))
worker['age'] = datetime.today().year - born
worker['ctps'] = int(input("Work license number: (0 if you dont have): "))
if worker['ctps'] != 0:
    worker['hireY'] = int(input("Hire year: "))
    worker['salary'] = float(input("Salary: "))
    worker['retiriment year'] = (worker["hireY"] + 35) - born
print("-="*30)
for k, v in worker.items():
    print(f"{k} got the value {v}")
