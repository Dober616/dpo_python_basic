import functools

count_funk = dict()
def decorator(func):
    count_funk[func.__name__] = 0
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
        count_funk[func.__name__] += 1



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


for key in count_funk.keys():
    print(f'Функция {key} вызывалась {count_funk[key]} раз')
