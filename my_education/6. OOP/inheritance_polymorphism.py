class Shape:
    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Drawing created')

    def area(self):
        print('Calc area')

    def perimeter(self):
        print('Calc perimeter')


class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height

        print('Rectangle created')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())


class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        print('Triangle created')

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(3, 4, 5)
print(triangle.perimeter())

shape = Shape()

for shape in [rectangle, triangle]:
    print(shape.perimeter())
