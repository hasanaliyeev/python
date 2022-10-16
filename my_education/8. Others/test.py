import random
import itertools
import time


def randoms(mini, maxi):
    while True:
        yield random.randint(mini, maxi)


rand = randoms(1, 10000)
n = itertools.islice(rand, 10)
for i in n:
    print(i)
