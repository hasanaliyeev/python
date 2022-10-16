class Character:
    def __init__(self):
        self.race = 'Elf'


c = Character()
print(c.race)


class Character:
    def __new__(cls):
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        self.race = 'Elf'


c = Character()
print(c.race)
