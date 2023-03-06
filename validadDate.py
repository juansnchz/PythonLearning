import leapyear

def isValidDate(year, month, date):
    if not (1 <= month <= 12):
        return False
    if leapyear.isLeapYear(year) and month == 2 and date == 29:
        return True
    if leapyear.isLeapYear(year) == False and month == 2 and not (1<=date<=28):
        return False
    if month in (1,3,5,7,8,10,12) and not (1<= date<=31):
        return False
    elif month in (4,6,9,11) and not (1<= date <= 30):
        return False

    return True



assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)

for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
