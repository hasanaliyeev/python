import math
import timeit


def decorator(func):
    def wrap(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        end = timeit.default_timer()
        print(f'Time: {(end - start): 0.5f}')

    return wrap


@decorator
def factorial(number):
    print(math.factorial(number))


factorial(10)


def my_decorator(func):
    def wrap(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')

    return wrap


@my_decorator
def average_salary(**kwargs):
    total_salary = sum(kwargs.values())
    month = len(kwargs)
    print(f'Total salary: {total_salary} RUB')
    av_slr = total_salary / month
    print(f'Average salary: {av_slr} RUB')


average_salary(january=35000, february=45000, mart=60000, april=70000)
