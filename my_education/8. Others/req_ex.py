import requests

a = 100
b = 100
c = {'a': 1, 'b': 100}


class A:
    def __init__(self):
        self.a_number = 100


class B:
    def __init__(self):
        self.b_number = 100


a1 = A()
b1 = B()
print(id(a), id(b), id(c.get('b')), id(a1.a_number), id(b1.b_number))