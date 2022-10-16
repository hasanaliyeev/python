from collections import namedtuple


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}   age: {self.age}'

    def __repr__(self):
        return f'Person("{self.name}, {self.age}")'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False


p4 = Person('Alsu alieva', 3)
p5 = Person('Gyunel Alieva', 27)
p1 = Person('Gasan Aliev', 30)
p3 = Person('Farid Aliev', 27)
p2 = Person('Gasan Aliev', 30)

persons = list()
persons.extend([p1, p2, p3, p4, p5])
print(persons)

print(list(filter(lambda x: x.age > 27, persons)))
