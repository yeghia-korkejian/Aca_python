import datetime
import time
import calendar
a = datetime.datetime.now()
five_days = datetime.timedelta(days = 5)
print(a)
print(a.year)
print(a.month)
print(a.isoweekday())
print(a - five_days)
print(a + five_days)