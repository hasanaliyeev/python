class Character:
    max_speed = 100
    dead_health = 0

    def __init__(self, name, damage=10, armor=20):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health


unit = Character('Gasan Aliev')
print(Character.max_speed)
print(unit.name)
print(unit.armor)
print(unit.damage)
print(unit.health)
unit.hit(25)
print(unit.health)
print(unit.is_dead())
unit.hit(75)
print(unit.is_dead())

