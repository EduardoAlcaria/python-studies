from datetime import datetime
worker = dict()
worker['name'] = str(input("Name: "))
born = int(input("Born year: "))
worker['age'] = datetime.today().year - born 
worker['ctps'] = int(input("CTPS: (0 if you dont have): "))
if worker['ctps'] == 0:
    for k, v in worker.items():
        print(f"{k} has the value {v}")
else:
    worker['hireY'] = int(input("Hire year: "))
    worker['retirement'] = (worker['hireY'] - born) + 35
    worker['salary'] = float(input("First salary: "))
    for k, v in worker.items():
        print(f"{k} has the value {v}")
    