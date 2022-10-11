class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age}'


gasan = Person('Gasan Aliev', 30)
alsu = Person('Alsu Alieva', 3)
print(gasan)
