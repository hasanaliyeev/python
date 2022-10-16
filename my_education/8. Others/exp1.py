class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return f'{self.__name}  {self.__age}  {self.__salary}'


class Work:
    def __init__(self):
        self.__employees = list()

    def add_emp(self, emp):
        self.__employees.append(emp)

    def get_employees(self):
        return self.__employees


work = Work()
emp1 = Employee('Gasan Aliev', 30, 60000)
emp2 = Employee('Farid Aliev', 27, 47000)
emp3 = Employee('Gunnel Alieva', 27, 42000)

work.add_emp(emp1)
work.add_emp(emp2)
work.add_emp(emp3)

print(work.get_employees())

