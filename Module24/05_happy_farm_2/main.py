
class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас в стадии {Potato.states[self.state]}')


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def are_all_ripe(self):
        if not all([some_potato.is_ripe() for some_potato in self.potatoes]):
            print('Еще не вся картошка созрела')
        else:
            print('Вся картошка созрела')

    def grow_all(self):
        print('Картошка растет')
        for some_potato in self.potatoes:
            some_potato.grow()

class Farmer:
    def __init__(self, name, collected_potatoes):
        self.name = name
        self.collected_potatoes = collected_potatoes

    def farmer_info(self):
        print(f'Садовника зовут {self.name}, собрано урожая {self.collected_potatoes}')

    def tend(self, my_garden):
        if all([some_potato.is_ripe() for some_potato in my_garden.potatoes]):
            question = input('Собрать картошку?(да/нет): ')
            if question == 'да':
                potato_count = 0
                for some_potato in my_garden.potatoes:
                    self.collected_potatoes += 1
                    potato_count += 1
                    some_potato.state = 0
                print(f'{self.name} собрал {potato_count} картошек')
                self.farmer_info()
        else:
            question = input(f'{self.name}у продолжить ухаживать за картошкой?(да/нет): ')
            if question == 'да':
                my_garden.grow_all()
                my_garden.are_all_ripe()

my_farm = Garden(5)
my_worker = Farmer('Петрович', 0)
while True:
    Farmer.tend(my_worker, my_farm)


