class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return 'Шторм'
        elif isinstance(other, Fire):
            return 'Пар'
        elif isinstance(other, Earth):
            return 'Грязь'
    def __str__(self):
        return 'Вода'


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return 'Молния'
        elif isinstance(other, Earth):
            return 'Пыль'
        elif isinstance(other, Water):
            return 'Шторм'
    def __str__(self):
        return 'Воздух'


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return 'Лава'
    def __str__(self):
        return 'Огонь'


class Earth:
    def __str__(self):
        return 'Земля'



water = Water()
air = Air()
earth = Earth()
fire = Fire()

print(water + air)
