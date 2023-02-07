import random

class Inhabitant:
    def __init__(self, name, living_house):
        self.name = name
        self.living_house = living_house
        self.satiety = 50


    def eat(self):
        if self.living_house.food >= 10:
            self.satiety += 10
            House.food -= 10
            print(f'Поели. Сытость {self.name} повысилась на 10 и стала равна {self.satiety}\n'
                  f'А вот еды в доме осталось {self.living_house.food}')
        elif House.food > 0:
            self.satiety += House.food
            House.food = 0
            print(f'Поели. Сытость {self.name} повысилась на {self.living_house.food} и стала {self.satiety}\n'
                  f'Зато продуктов больше не осталось.')
        else:
            print('Так нечего вам есть идите работайте.')

    def work(self):
        self.satiety -= 10
        House.money += 10
        print(f'Поработали. Сытость уменишилась на 10 и стала {self.satiety}\n'
              f'Зато денег прибавилось на 10 и стало {House.money}')


    def shopping(self):
        if House.money >= 10:
            self.living_house.food += 10
            House.money -= 10
            print(f'Сходили в магазин и купили продуктов. Денег стало на 10 меньше и стало {House.money}\n'
                f'Зато еды в доме прибавилось и стало {self.living_house.food}')
        elif House.money > 0:
            self.living_house.food += House.money
            House.money -= House.money
            print(f'Сходили в магазин и купили {self.living_house.food} продуктов. Денег больше не осталось.')
        else:
            print('Так не на что в магазин идти, иди работай')

    def actions(self):
        if self.satiety < 20:
            self.eat()
        elif self.living_house.food < 10:
            self.shopping()
        elif House.money < 50:
            self.work()
        else:
            roll_the_dice = random.randint(1, 6)
            if roll_the_dice == 1:
                self.work()
            elif roll_the_dice == 2:
                self.eat()


class House:
    food = 50
    money = 0


max = Inhabitant('Максим', 'My_house')
molly = Inhabitant('Молли', 'My_house')
for day in range(365):
    print(f'День {day + 1}')
    max.actions()
    if max.satiety < 0:
        print(f'Игра окончена, {max.name} умер')
        break
    molly.actions()
    if molly.satiety < 0:
        print(f'Игра окончена, {molly.name} умерла')
        break
