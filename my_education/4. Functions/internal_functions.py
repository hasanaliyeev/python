a = abs(-1)
print(a)

b = max(1, 2, 3, 4)
print(b)

players = [('a', 17), ('B', 15), ('c', 67)]
p = all([rating > 10 and x.islower() for x, rating in players])
print(p)

pairs = [False, True, False, True]
my_any = any(pairs)
print(my_any)

letters = ('a', 'b', 'c', 'd')
numbers = (1, 2, 3)
zipped = zip(letters, numbers)
print(list(zipped))

code = ord('e')
print(code)

char = chr(120)
print(char)
