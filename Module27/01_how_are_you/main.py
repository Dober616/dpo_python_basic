import functools
def how_are_you(func):
    @functools.wraps(func)
    def wrapped_func():
        question = input('Как дела? Пожалуйста ответьте: ')
        result = func()
        return result
    return wrapped_func

@how_are_you
def test():
    print(f'Тут что-то происходит. Выполняется функция {test.__name__}')

test()

