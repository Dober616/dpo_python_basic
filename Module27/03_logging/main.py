from datetime import datetime
import time
import functools


def logging(func):
    @functools.wraps(func)
    def wrapped_funk(*args, **kwargs):
        print(f'Имя фукции: {func.__name__}\n'
              f'Документация: {func.__doc__}')
        try:
            result = func(*args, **kwargs)
            return result
        except BaseException:
            with open('log.txt', 'w') as file:
                file.write(f'Дата/время: {datetime.now()}\n'
                           f'имя функции: {func.__name__}\n'
                           f'документация: {func.__doc__}\n')
    return wrapped_funk


@logging
def my_function():
    """
    функция создающая список от 0 до 9
    с выводом несуществующего индекса списка
    """
    my_list = [i for i in range[10]]

    return my_list[11]

print(my_function())