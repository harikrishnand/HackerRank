import calendar as cal

mon,date,year = map(int, input().split())

#print(mon,date,year)

print(cal.day_name[cal.weekday(year,mon,date)].upper())
