import math

numbers = [1, 2, 3, 4]


class Character:

    def __init__(self, name, age=30):
        self.name = name
        self.age = age

    def factorial(self, number):
        return math.factorial(number)


unit = Character('Gasan Aliev')
print(unit.factorial(6))
print(unit.name)
print(unit.age)
