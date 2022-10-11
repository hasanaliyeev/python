class Animal:
    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage


class Carnivore(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4


c = Carnivore()
c.hit(10)
print(c.health)
