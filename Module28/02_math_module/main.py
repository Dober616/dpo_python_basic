import math


class MyMath:
    @staticmethod
    def summ(a, b):
        return a + b

    @staticmethod
    def round_length(radius):
        print('Длина окружности: ', end='')
        return 2 * math.pi * radius

    @staticmethod
    def round_square(radius):
        print('Площадь круга: ', end='')
        return math.pi * radius**2

    @staticmethod
    def cube_volume(side):
        print('Объем круга: ', end='')
        return side**3

    @staticmethod
    def sphere_surface(radius):
        print('Площадь поверхности сферы: ', end='')
        return 4 * math.pi * radius**2


print(MyMath.summ(5, 6))
print(MyMath.round_length(radius=3))
print(MyMath.round_square(radius=3))
print(MyMath.cube_volume(4))
print(MyMath.sphere_surface(3))
