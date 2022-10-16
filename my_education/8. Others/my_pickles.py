class Character:

    def __init__(self, race, armor, damage=10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')
        self.armor = state.get('armor', 20)
        self.damage = state.get('damage', 10)
        self.health = state.get('health', 100)


c = Character('Elf', 30)
c.hit(10)
