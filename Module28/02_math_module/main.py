import math
class MyMath:
    def __init__(self, side_1=0, side_2=0, side_3=0, radius=0):
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3
        self._radius = radius

    @property
    def side_1(self):
        return self._side_1

    @side_1.setter
    def side_1(self, side_1):
        if side_1 > 0:
            self._side_1 = side_1
        else:
            raise Exception('Не может быть меньше нуля')\

    @property
    def side_2(self):
        return self._side_2

    @side_2.setter
    def side_2(self, side_2):
        if side_2 > 0:
            self._side_2 = side_2
        else:
            raise Exception('Не может быть меньше нуля')

    @property
    def side_3(self):
        return self._side_3

    @side_3.setter
    def side_3(self, side_3):
        if side_3 > 0:
            self._side_3 = side_3
        else:
            raise Exception('Не может быть меньше нуля')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise Exception('Не может быть меньше нуля')

    @property
    def circle_len(self):
        return  2 * math.pi * self._radius


res = MyMath(radius=4).circle_len
print(res)


