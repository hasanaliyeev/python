import unittest
from constants import Character


class CharacterTest(unittest.TestCase):

    def test_average_salary(self):
        unit = Character('Gasan')
        salaries = [100, 200, 300, 400]
        result = unit.average_salary(salaries)
        self.assertEquals(result, 250.0)
