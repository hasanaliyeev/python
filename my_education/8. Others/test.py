import random
import itertools
from random_name import MyGame
import time


def randoms(mini, maxi):
    while True:
        yield random.randint(mini, maxi)


rand = randoms(1, 10000)
n = itertools.islice(rand, 10)
for i in n:
    print(i)

g = MyGame()
g.start(1)
