import json


class Person:

    def __init__(self, lastname, firstname, age, city):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.city = city
        self.phones = list()
        self.children = list()

    def add_phone(self, phone):
        self.phones.append(phone)

    def add_child(self, lastname, firstname, age, phone):
        ch = dict()
        ch.setdefault('lastname', lastname)
        ch.setdefault('firstname', firstname)
        ch.setdefault('age', age)
        ch.setdefault('phone', phone)
        self.children.append(ch)

    def __repr__(self):
        return f'Person("{self.lastname}, {self.firstname}, {self.age}, {self.city}, {self.phones}")'

    def __str__(self):
        return f'{self.lastname} {self.firstname}'


gasan = Person('Aliev', 'Gasan', 30, 'Volgodonsk')
gasan.add_phone('+7 (928) 187-06-02')
gasan.add_phone('+7 (900) 134-75-75')
gasan.add_child('Family', 'Name', 'age', 'phone')
gasan.add_child('Alieva', 'Alsu', 3, '+7 (900) 134-75-75')

json_data = json.dumps(gasan, default=lambda obj: obj.__dict__)
print(json_data)



# with open(r'C:\Users\aliye\Desktop\GitHub\python\my_education\8. Others\persons.json', 'w') as file:
#   json.dump(gasan.__dict__, file)
