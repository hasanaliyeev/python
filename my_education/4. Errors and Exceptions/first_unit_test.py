import unittest
import fizz_buzz


class FizzBuzzTests(unittest.TestCase):
    def test_fizz(self):
        number = 6
        result = fizz_buzz.get_reply(number)
        self.assertEquals(result, 'Fizz')

    def test_buzz(self):
        number = 10
        result = fizz_buzz.get_reply(number)
        self.assertEquals(result, 'Buzz')

    def test_fizz_buzz(self):
        number = 15
        result = fizz_buzz.get_reply(number)
        self.assertEquals(result, 'FizzBuzz')
