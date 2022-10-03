#  Реализуйте одну классическую и достаточно простую игру: "угадай число".
import random


def guess(attempt=6):
    number = random.randint(1, 50)
    count = 0
    while count < attempt:
        inp = int(input('Введите число: '))
        if inp < number:
            print('Загаданое число меньше')
        elif inp > number:
            print('Загаданое число больше')
        else:
            print('Число отгадано - ', inp)
            return
        count += 1
    print(f'Число: {number}')


guess(3)
