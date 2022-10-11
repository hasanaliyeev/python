from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        print('Shape class drawing')

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print('Rectangle created')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        super().draw()


rectangle = Rectangle(4, 5)
rectangle.draw()
print(rectangle.area())
print(rectangle.perimeter())
