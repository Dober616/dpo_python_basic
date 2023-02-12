class MyMath:
    def __init__(self, a, b):
        self.a(a)
        self.b(b)

    @property
    def a(self):
        return self.a

    @a.setter
    def a(self, a):
        self.a = a

    @property
    def b(self):
        return self.b

    @b.setter
    def b(self, b):
        self.b = b

    def summ(self):
        return self.a() + self.b()

res = MyMath.summ(4, 4)