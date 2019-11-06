import datetime
import time
import calendar
bday = datetime.date(1994, 1, 3)
print (bday)
print (bday.year)
print (bday.month)
print (bday.day)
print (bday.isoweekday())
upcoming_bday = datetime.date(2020, 1, 3)
tday = datetime.date.today()
till_bday = upcoming_bday - tday
print (till_bday.days)
cal = calendar.month(2017, 5)
print (cal)
today = datetime.datetime.today()
one_day = datetime.timedelta(days = 1)
yesterday = today - one_day
print (yesterday)
add_two = yesterday + one_day*2
print (add_two)
sub_three = yesterday - one_day*3
print (sub_three)