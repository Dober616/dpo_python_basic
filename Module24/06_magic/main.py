class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Stream()
        elif isinstance(other, Earth):
            return Grease()

    def __str__(self):
        return 'Вода'


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Ligtning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()

    def __str__(self):
        return 'Воздух'


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava

    def __str__(self):
        return 'Огонь'


class Earth:
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return 'Шторм'


class Stream:
    def __str__(self):
        return 'Пар'


class Grease:
    def __str__(self):
        return 'Грязь'


class Ligtning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
earth = Earth()
fire = Fire()
storm = Storm()
stream = Stream()
grease = Grease()
lightning = Ligtning()
dust = Dust()
lava = Lava()


print(f'{air} + {water} = {air + water}')
print(f'{air} + {fire} = {air + fire}')
