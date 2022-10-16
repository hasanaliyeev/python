from enum import Enum
from enum import IntEnum
from enum import IntFlag


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


print(TrafficLight.RED.name)
print(TrafficLight.RED.value)

print(TrafficLight(1))
print(TrafficLight['RED'].name)


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Color(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4


combination = Color.RED | Color.BLUE
print(combination)
print(Color.RED in combination)


class Planet(Enum):
    MERCURY = (3.303e+23, 2.23e+2)
    EARTH = (5.6788e+3, 7.67e+67)
    JUPITER = (1.9e+27, 7.14e+7)


print(Planet.EARTH.value)
