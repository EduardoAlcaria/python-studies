studant = dict()
studant_array = list()
studant["name"] = str(input("Name: "))
studant["grade"] = float(input("Avarage grade: "))
studant_array.append(studant.copy())
for s in studant_array:
    for k, v in s.items():
        print(f"{k} is igual to {v}")
if studant_array[0]["grade"] >= 7:
    print("the situation is APROVED")
else:
    print("the situation is REPROVED")