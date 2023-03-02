import datetime
import math
# get the dates from the user
print("**The format of the date YYYY-MM-DD")
date1 = input("Enter the First date: ")
date2 = input("Enter the Second date: ")
# change the dates to be a date object
date1_as_datetime = datetime.datetime(year=int(date1[0:4]), month=int(date1[5:7]), day=int(date1[8:]))
date2_as_datetime = datetime.datetime(year=int(date2[0:4]), month=int(date2[5:7]), day=int(date2[8:]))
# getting the time difference
time_difference = date1_as_datetime - date2_as_datetime
days = int(str(time_difference).split()[0])
print(int(math.fabs(days * 24)))
