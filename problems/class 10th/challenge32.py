from datetime import date
year = int(input('Type a year or type 0 to analize the current year: '))
if year == 0:
    year = date.today().year
if year%4 == 0 and year%100 != 0 or year % 400 == 0:
    print('the year {} is a leap year'.format(year))
else:
    print('the year {} is a normal year'.format(year))