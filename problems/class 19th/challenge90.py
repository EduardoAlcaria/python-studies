studant = dict()
studant['name'] = str(input("Studant name: "))
studant['avGrade'] = float(input("Avarege grade: "))
if studant['avGrade'] >= 7:
    studant['status'] = "APROVED"
elif studant['avGrade'] >= 5 and studant['avGrade']< 7:
    studant['status'] = "RECOVERY EXAM"
else:
    studant["status"] = "REPROVED"
for k, v in studant.items():
    print(f"{k} has the value {v}")