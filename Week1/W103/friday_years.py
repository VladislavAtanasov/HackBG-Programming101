def friday_years(start,end):
    import calendar
    count = 0
    for x in range(start,end+1):
        if (calendar.weekday(x,1,1) == 4 and calendar.isleap(x) == False) or ((calendar.weekday(x,1,1) == 4 or calendar.weekday(x,1,2) == 4) and calendar.isleap(x)):
            count += 1
    return count

print(friday_years(1000, 2000))
print(friday_years(1753, 2000))
print(friday_years(1990, 2015))
