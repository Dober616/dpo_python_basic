def how_are_you(func):
    def wrapped_func():
        question = input('Как дела? Пожалуйста ответьте: ')
        result = func()
        return result
    return wrapped_func

@how_are_you
def test():
    print('Тут что-то происходит...')

test()

