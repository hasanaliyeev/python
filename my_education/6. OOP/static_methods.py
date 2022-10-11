class StaticTest:
    x = 1


t1 = StaticTest()
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')

t1.x = 2
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')

StaticTest.x = 3
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        day = str(self.day).rjust(2, '0') if self.day < 10 else self.day
        month = str(self.month).rjust(2, '0') if self.month < 10 else self.month
        return f'{day}-{month}-{self.year}'


date = Date(30, 6, 1992)
print(date.display())
