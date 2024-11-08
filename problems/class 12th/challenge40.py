n1 = float(input('Type the 1st grade: '))
n2 = float(input('Type the 2nd grade: '))
grade = (n1 + n2) / 2
if grade < 5:
    print('REFUCED\nGRADE: {:.1f}'.format(grade))
elif grade >= 5 and grade < 7:
    print('RECOVERY EXAMS\nGRADE: {:.1f}'.format(grade))
else:
    print('APPROVED\nGRADE: {:.1f}'.format(grade))
