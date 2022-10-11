class Character:
    _age = 30
    __salary = 60000
    city = 'Volgodonsk'
    MAX_YEAR = 45

    def __init__(self, name, damage=10):
        self.__name = name
        self.damage = damage
        self._health = 100
        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    def get_info(self, profession):
        print(f'My name is {self.__name}. I\'m {self._age}. I live in {self.city}. My salary {self.__salary}. '
              f'I {profession} specialist.')

    @property
    def health(self):
        return self._health

    @property
    def name(self):
        return self.__name

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed

    def average_salary(self, salary):
        months = len(salary)
        total_salary = sum(salary)
        return total_salary / months


unit = Character('Gasan Aliev')
unit.get_info('Python')
unit.hit(27)
print(unit.health)
print(unit.name)
unit.current_speed = 60
print(unit.current_speed)
print(unit.average_salary([100, 200, 300, 400]))
