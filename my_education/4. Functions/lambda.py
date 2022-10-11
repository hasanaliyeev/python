def func(n):
    return lambda i: i ** n


square = func(2)
numbers = [2, 3, 4, 5]
mapped = list(map(square, numbers))
x = map(lambda a, b: {a: b}, numbers, mapped)
print(list(x))


def is_adult(n):
    return lambda i: i >= n


adult = is_adult(18)
print(adult(20))

is_young = lambda i: i < 35
gasan_age = is_young(30)
print(gasan_age)

ages = [12, 6, 67, 45, 16, 26, 36]
young = list(filter(is_young, ages))
print(young)
