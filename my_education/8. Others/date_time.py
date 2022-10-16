from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import locale

locale.setlocale(locale.LC_ALL, '')

d1 = date.today()
print(d1)
d2 = date(1992, 6, 30)
print(d2)

dt1 = datetime.now()
print(dt1)
dt2 = datetime(2019, 9, 1, 11, 0, 0)
print(dt2)

s = '13.10.2022'
ds = datetime.strptime(s, '%d.%m.%Y')
print(ds)

d3 = date.today()
s1 = d3.strftime('%d.%m.%Y %A')
print(s1)

dt3 = datetime.now()
print(dt3.time())

td = timedelta(days=10, hours=26, minutes=78)
print(td)

my_birth = date(1992, 6, 30)
today = date.today()
c = today - my_birth
print(f'Разница: {c.days}')

my_date = datetime(1992, 6, 30, 11, 35, 7)
my_date_str = my_date.strftime('%d.%m.%Y %A %H:%M:%S')
print(my_date_str)
print()

print(datetime.now().strftime('%d %B %Y %H:%M:%S  (%c) '))



