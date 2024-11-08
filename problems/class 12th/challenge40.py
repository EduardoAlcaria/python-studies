n1 = float(input('Type the 1st grade: '))
n2 = float(input('Type the 2nd grade: '))
grade = (n1 + n2) / 2
if grade <= 5.0:
    print('REFUCED\nGRADE: {}'.format(grade))
elif grade > 5.0 and grade < 6.9:
    print('RECOVERY EXAMS\nGRADE: {}'.format(grade))
else:
    print('APPROVED\nGRADE: {}'.format(grade))
