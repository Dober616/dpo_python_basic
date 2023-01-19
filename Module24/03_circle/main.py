import math


class Circle:

    def __init__(self, name='first',  x=0, y=0, radius=1):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius

    def print_info(self):
        print(f'{self.x}, {self.y}, {self.radius}')

    def circle_square(self):
        return math.pi * self.radius**2

    def circle_perimetr(self):
        return 2 * math.pi * self.radius

    def info(self):
        print(f'Площадь окружности {self.name}: {self.circle_square()}\n'
              f'Периметр окружности {self.name}: {self.circle_perimetr()}')


def dots_line(crcl1, crcl2):
    dots_distanse = math.sqrt((crcl1.x - crcl2.x) ** 2) +\
                    ((crcl1.y - crcl2.y) ** 2)
    if dots_distanse > crcl1.radius + crcl2.radius:
        print('Не пересекаются')
    else:
        print('Пересекааются')


my_circle = Circle()
my_circle.info()
new_circle = Circle('second', 4, 1, 1)
new_circle.info()
dots_line(my_circle, new_circle)
