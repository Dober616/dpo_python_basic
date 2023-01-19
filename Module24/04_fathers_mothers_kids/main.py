class Parents:
    def __init__(self, name, age, clildren):
        self.name = name
        self.age = age
        self.children = []

    def parent_info(self):
        print(f'Информация о родителе {self.name}:\n'
              f'Возраст: {self.age}\n'
              f'Дети: {self.children}')

    def actions(self, child):
        if self.age - child.age >= 16:
            if child.chill == 0:
                print(f'Ребенок {child.name} спокоен, все в порядке')
            else:
                while child.chill > 0:
                    print(f'Родитель {self.name} утешает ребенка {child.name}')
                    child.chill -= 1
                print(f'Наконец-то ребенок {child.name} успокоился')
            if child.hungry == 0:
                print(f'Ребенок {child.name} сыт, все в порядке')
            else:
                while child.hungry > 0:
                    print(f'Родитель {self.name} кормит ребенка {child.name}')
                    child.hungry -= 1
                print(f'Ребенок {child.name} сыт')
        else:
            print(f'Ребенок {child.name} то уже не ребенок')



class Kid:
    def __init__(self, name, age, chill, hungry):
        self.name = name
        self.age = age
        self.chill = chill
        self.hungry = hungry

    def childrens_info(self):
        print(f'Информация о ребенке {self.name}:\n'
              f'Возраст: {self.age}\n'
              f'Cостояние спокойствия: {self.chill}\n'
              f'Состояние голода: {self.hungry}')

import random

parent = Parents(input('Имя родителя: '), int(input('Возраст: ')), clildren=[])
child_1 = Kid(input('Имя ребенка: '), int(input('Возраст ребенка: ')), random.randint(0, 3), random.randint(1, 3))
parent.children.append(child_1)
child_2 = Kid(input('Имя ребенка: '), int(input('Возраст ребенка: ')), random.randint(0, 3), random.randint(1, 3))
parent.children.append(child_2)

for child in parent.children:
    parent.actions(child)
