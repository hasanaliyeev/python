import random
import itertools


def randoms(minimum, maximum, count):
    return [random.randint(minimum, maximum) for _ in range(count)]


rand_sequence = randoms(1, 10, 10)
print(rand_sequence)
print(rand_sequence)


def randoms(minimum, maximum, count):
    for n in range(count):
        yield random.randint(minimum, maximum)


rand_sequence = randoms(1, 10, 10)
print([i for i in rand_sequence])
print([i for i in rand_sequence])


def randoms(minimum, maximum, count):
    for i in range(count):
        yield random.randint(minimum, maximum)


rand_sequence = randoms(1, 10, 10)
seven_taken = list(itertools.islice(rand_sequence, 7))
print(f'Seven: {seven_taken}')
print([i for i in rand_sequence])


def randoms(minimum, maximum):
    while True:
        yield random.randint(minimum, maximum)


rand_sequence = randoms(1, 100000)
rand_number = list(itertools.islice(rand_sequence, 10))
print(rand_number)

n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)
