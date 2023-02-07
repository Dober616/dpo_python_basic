import functools


def debug(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'Вызывается: {func.__name__}{args})\n'
              f'{func.__name__} вернула значение {repr(func(*args))}')
        print(func(*args, **kwargs))
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return f'Привет, {name}! Тебе уже {age} лет! Как быстро ты растешь!\n'
    else:
        return f'Привет, {name}\n'


greeting('Кирилл', 38)
greeting('Егор')
greeting('Катя', 16)
