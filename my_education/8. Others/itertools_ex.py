import itertools
import numbers

iterable = [1, 2, 3, 4, 5, 6]

iterator = iter(iterable)
print(type(iterator))

print(next(iterator))

sequence = list(itertools.islice(iterator, 2))
print(sequence)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_numbers = itertools.count(1, 2)
print(list(next(even_numbers) for i in range(5)))

t = list(zip(itertools.count(), ['a', 'b']))
print(t)

ones = itertools.repeat(1, 5)


def print_iterable(itr, end=None):
    for x in itr:
        if end:
            print(x, end=end)
        else:
            print(x)


print(print_iterable(ones, ' '))

my_list = list(map(pow, range(10), itertools.repeat(2)))
print(my_list)

rep = itertools.count(10, 10)
nums = [next(rep) for _ in range(10)]
print(nums)
print(next(rep))
new_nums = list(itertools.islice(rep, 10))
print(new_nums)
print()

letters = itertools.cycle(['A', 'B', 'C', 'D'])
cycle_letters = list(next(letters) for _ in range(10))
print(cycle_letters)

nums = itertools.cycle([-1, 1])
cycle_nums = list(next(nums) for _ in range(10))
print(cycle_nums)
print()

acc = itertools.accumulate([1, 2, 3, 4, 5, 6])
print(list(acc))
acc = itertools.accumulate([3, 2, 3, 7, 5], max)
print(list(acc))

ch = itertools.chain.from_iterable(['Gasan', 'Farid'])
print(list(ch))
ch = itertools.chain('Gasan', 'Farid')
print(list(ch))

drop_w = itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5, 7, 1])
print(list(drop_w))

take_w = itertools.takewhile(lambda x: x < 3, [1, 2, 5, 1, 2, 3, 4, 5, 6])
print(list(take_w))

