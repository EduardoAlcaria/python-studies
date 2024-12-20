studant = dict()
studant['name'] = str(input("Name: "))
studant['grade'] = float(input(f"Avarege grade of {studant['name']}: "))
if studant['grade'] >= 7:
    studant['status'] = "APROVED"
elif studant['grade'] >= 5 or studant['grade'] < 7:
    studant['status'] = "RECOVERY TEST"
else:
    studant['status'] = "REPROVED"
print()
for k,v in studant.items():
    print(f"{k} is igual to {v}")