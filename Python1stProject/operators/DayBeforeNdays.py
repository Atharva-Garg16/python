# 0 sun; 1 mon; 2 tue; 3 wed; 4 thurs; 5 fri; 6 sat
day=int(input("enter the day\n"))
DaysBefore=int(input("enter n days before to find\n"))
print((day-DaysBefore)%7)