studants = list()
fGrade = 0
while True:
    name = str(input("Studant: "))
    grade1 = float(input("Grade 1: "))
    grade2 = float(input("Grade 2: "))
    fGrade = (grade1+grade2)/2
    studants.append([name, [grade1, grade2], fGrade])
    ask_continue = str(input("Want to continue? [y/n]: ")).strip()
    if ask_continue in "nN":
        break
print("-=" * 30)
print(f"{'N' : <4} {'Name'.capitalize(): <10} {'F.Grade' :>10}")
for e, s in enumerate(studants):
    print(f"{e : <4} {s[0] : <10} {s[2]:>10.1f}")
print("-="*30)
choice = 0
while choice != 999:
    choice = int(input("Show the grade of which studant? (999 to stop): "))
    for e,s in enumerate(studants):
        if choice == e:
            print(f"The {s[0]}'s grades are {s[1]}")