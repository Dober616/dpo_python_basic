import functools


def decorator(func):
    count_funk = dict()
    count_funk[func.__name__] = 0
    def wrapped_func(*args, **kwargs):
        count_funk[func.__name__] += 1
        func(*args, **kwargs)
        print(f'Функция {func.__name__} вызывалась {count_funk[func.__name__]} раз')
    return wrapped_func


@decorator
def my_func():
    pass

@decorator
def ttt():
    pass

my_func()
my_func()
for i in range(5):
    ttt()




