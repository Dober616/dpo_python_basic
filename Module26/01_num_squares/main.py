class Iterator:
    def __init__(self, n):
        self.numm = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.numm += 1
        if self.numm > self.n:
            raise StopIteration
        return self.numm ** 2


my_iterator = Iterator(10)
for i in my_iterator:
    print(i, end=' ')
print('\n')


def my_generator(n):
    for i in range (1, n+1):
        yield i ** 2

for i in my_generator(10):
    print(i, end=' ')
print('\n')

my_gen = (x ** 2 for x in range(1, 11))
for i in my_gen:
    print(i, end=' ')