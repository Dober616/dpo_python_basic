import random


class Warrior:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print(f'У воина {self.name} осталось {self.health} очков здоровья')

    def fight(self):
        while self.health > 0:
            kick = random.randint(0, 1)
            if warriors[abs(kick - 1)].health <= 0:
                print('Битва окончена')
                break
            else:
                print(f'Атакует {warriors[kick].name}')
                warriors[abs(kick - 1)].health -= 20
                print(warriors[abs(kick - 1)].info())


warrior_1 = Warrior('Иван', 100)
warrior_2 = Warrior('Егор', 100)

warriors = [warrior_1, warrior_2]
for warrior in warriors:
    warrior.fight()
