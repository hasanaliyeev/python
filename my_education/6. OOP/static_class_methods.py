class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f'{self.day}-{self.month}-{self.year}'

    @staticmethod
    def static_method(day, month):
        return Date(day, month, 2000)

    @classmethod
    def class_method(cls, day, month):
        return cls(day, month, 2000)


d1 = Date.static_method(11, 10)
d2 = Date.class_method(11, 10)
print(d1.display(), isinstance(d1, Date))
print(d2.display(), isinstance(d2, Date))

date = Date(11, 10, 2022)
print(date.display(), isinstance(date, Date))


class DateTime(Date):
    def display(self):
        return f'{self.day}-{self.month}-{self.year}  00:00:00'


d1 = DateTime(30, 6, 1992)
print(d1.display(), isinstance(d1, DateTime))

d2 = DateTime.class_method(30, 6)
print(d2.display(), isinstance(d2, DateTime))

d3 = DateTime.static_method(30, 6)
print(d3.display(), isinstance(d3, DateTime))

date_time = DateTime(11, 10, 2022)
print(date_time.display(), isinstance(date_time, DateTime))
print(date_time.static_method(11, 11).display())
print(date_time.class_method(11, 11).display())
