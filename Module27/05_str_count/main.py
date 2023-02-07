
def my_counter(func):
    count = 0
    def wrapped_func(*args, **kwargs):

        result = func(*args, **kwargs)
        return result

    count += 1
    print(count)
    return wrapped_func


@my_counter
def my_func():
    pass

@my_counter
def ttt():
    pass

my_func()
for i in range(5):
    ttt()


