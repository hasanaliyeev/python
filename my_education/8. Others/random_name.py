import random
from enum import Enum
import time
import itertools


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person("{self.name}")'

    def __str__(self):
        return f'{self.name}'


class Game:
    def __init__(self):
        self.__gamers = list()

    def add_gamers(self, *args):
        self.__gamers.extend(args)

    @property
    def gamers(self):
        return self.__gamers

    def remove(self, index):
        try:
            return self.__gamers.pop(index)
        except IndexError as ex:
            return ex

    @staticmethod
    def randoms(minimum, maximum):
        while True:
            yield random.randint(minimum, maximum - 1)

    def start(self):
        gamer_count = len(self.__gamers)
        losing_player_index = next(Game.randoms(0, gamer_count))
        print(f'Losing player: {self.remove(losing_player_index)}')
        print(f'Remaining players: {[i.name for i in self.__gamers]}')

    def winner(self):
        return len(self.__gamers) == 1


class MyGame:
    def __init__(self):
        self.game = Game()

    def start(self, load_time=1.0):
        gamers_in = input('Gamers: ')
        gamer_list = gamers_in.split()
        for i in range(len(gamer_list)):
            person = Person(gamer_list[i])
            self.game.add_gamers(person)

        while True:
            self.game.start()
            time.sleep(load_time)
            if not self.game.winner():
                continue
            else:
                print(f'Winner: {self.game.gamers[0]}')
                break


game = MyGame()
if '__main__' == __name__:
    while True:
        reply = float(input('Loading time: '))
        game.start(reply)

