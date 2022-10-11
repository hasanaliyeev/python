import timeit

file = None
try:
    print('Before try')
    file = open(r'C:\\Users\\aliye\\Desktop\\salary.txt')
    data = file.read()
    print(data)
    print('After try')
except FileNotFoundError as ex:
    print('Before exception')
    print(f'an error occurred {ex}')
    print('After exception')
finally:
    print('Start Finally')
    if file:
        print('Before close')
        file.close()
        print('After close')
    print('End Finally')


def time_decorator(func):
    def wrap(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        end = timeit.default_timer()
        print(f'Time: {(end-start):0.5f}')
    return wrap



@time_decorator
def get_int():
    while True:
        try:
            reply = int(input('Enter number: '))
            return reply
        except:
            print('Not a number. Try again...')
            continue


number = get_int()
print(number)


