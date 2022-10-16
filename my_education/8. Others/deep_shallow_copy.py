import copy

# Shallow copy
list1 = [1, 2, 3, [4, 5]]
list2 = copy.copy(list1)

list1.append(7)
list2[3].append(6)

print(list1)
print(list2)
print()

# Deep copy

list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

list1[2].append(5)
list2[2].append(7)

print(list1)
print(list2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


a = Point(2, 4)
b = copy.copy(a)
print(a)
print(b)
print()

b.b = 3
print(a)
print(b)
print()

l1 = Line(a, b)
l2 = copy.deepcopy(l1)
print(l1.p1, l1.p2)
print(l2.p1, l2.p2)
print()

l2.p2.x = 7
print(l1.p1, l1.p2)
print(l2.p1, l2.p2)







