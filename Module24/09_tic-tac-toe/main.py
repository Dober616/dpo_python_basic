

class Board:
    cells = {}
    for i in range(1, 10):
        cells[i] = ' '


class Player:
    def board_info(self):
        print(f'{Board.cells[1]}|{Board.cells[2]}|{Board.cells[3]}\n'
              f'__|__|__\n'
              f'{Board.cells[4]}|{Board.cells[5]}|{Board.cells[6]}\n'
              f'__|__|__\n'
              f'{Board.cells[1]}|{Board.cells[2]}|{Board.cells[3]}\n')

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play_game(self):
        self.sell_choose = int(input(f'Куда ходим, {self.name}? '))
        if Board.cells[self.sell_choose] == ' ':
            Board.cells[self.sell_choose] = self.symbol
        else:
            print('Ячейка занята')
            self.play_game()
        print(f' {Board.cells[1]} | {Board.cells[2]} | {Board.cells[3]} \n'
              f'___|___|___\n'
              f' {Board.cells[4]} | {Board.cells[5]} | {Board.cells[6]} \n'
              f'___|___|___\n'
              f' {Board.cells[7]} | {Board.cells[8]} | {Board.cells[9]} \n')


def rules():
    if Board.cells[1] == Board.cells[2] == Board.cells[3] and Board.cells[1] != ' ':
        print(f'Победил {Board.cells[1]}')
        return False
    elif Board.cells[1] == Board.cells[4] == Board.cells[7] and Board.cells[1] != ' ':
        print(f'Победил {Board.cells[1]}')
        return False
    elif Board.cells[1] == Board.cells[5] == Board.cells[9] and Board.cells[1] != ' ':
        print(f'Победил {Board.cells[1]}')
        return False
    elif Board.cells[3] == Board.cells[6] == Board.cells[9] and Board.cells[3] != ' ':
        print(f'Победил {Board.cells[3]}')
        return False
    elif Board.cells[7] == Board.cells[8] == Board.cells[9] and Board.cells[7] != ' ':
        print(f'Победил {Board.cells[7]}')
        return False


egor = Player('Егор', 'X')
serg = Player('Сергей', '0')
while True:
    egor.play_game()
    if rules() != False:
        serg.play_game()
    else:
        break
