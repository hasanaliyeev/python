from collections import namedtuple


def func(n):
    return lambda x: x ** n


square = func(2)
numbers = [2, 3, 4, 5]
mapped = list(map(square, numbers))
x = map(lambda a, b: {a: b}, numbers, mapped)
print(list(x))


def is_adult(n):
    return lambda x: x >= n


adult = is_adult(18)
print(adult(20))

is_young = lambda x: x < 35
gasan_age = is_young(30)
print(gasan_age)

ages = [12, 6, 67, 45, 16, 26, 36]
young = list(filter(is_young, ages))
print(young)

