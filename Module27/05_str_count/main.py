

class Counter:
    def __init__(self, count):
        self.count = count


class Func(Counter):
    def __init__(self, func, count=0):
        super().__init__(count)
        self.func = func

    def decorator(self):
        def wrapped_func(*args, **kwargs):
            return self.func()
            self.count += 1


        return wrapped_func



