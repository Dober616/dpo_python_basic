import random


class Card:
    suits = ['Пики', 'Крести', 'Буби', 'Черви']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_info(self):
        print(self.rank + ':' + self.suit)


class Deck:
    def __init__(self):
        self.cards = [(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deck_info(self):
        for card in self.cards:
            print(card[0] + ':' + card[1])


class Player:
    score = 0

    def __init__(self, name):
        self.name = name
        self.own_cards = []
        self.score = 0

    def player_info(self):
        print(f'{self.name}: побед - {self.score}')

    def own_cards_info(self):
        print(f'У {self.name} на руках: ')
        for own_card in self.own_cards:
            print(own_card[0] + ':' + own_card[1])

    def cards_count(self):
        count = 0
        for own_card in self.own_cards:
            if not own_card[1].isdigit():
                if own_card[1] == 'A' and count < 10:
                    count += 11
                elif own_card[1] == 'A' and count > 10:
                    count += 1
                else:
                    count += 10
            else:
                count += int(own_card[1])
        return count

    def cards_count_info(self):
        print(f' Количество очков у {self.name} равно {self.cards_count()}')

    def score_up(self):
        self.score += 1
        print(f'{self.name} выиграл!')


BJ_deck = Deck()
BJ_deck.shuffle()

player_1 = Player('Кирилл')
player_2 = Player('Егор')

while True:
    rep = input('Сыграем? Если да - "1", если нет - "0": ')
    if rep == '0':
        player_1.player_info()
        player_2.player_info()
        break
    elif rep == '1':
        if len(BJ_deck.cards) < 20:
            New_BJ_deck = Deck()
            New_BJ_deck.shuffle()
            BJ_deck = New_BJ_deck

        player_1.own_cards = []
        player_2.own_cards = []

        player_1.own_cards.append(BJ_deck.cards.pop())
        player_1.own_cards.append(BJ_deck.cards.pop())
        player_1.own_cards_info()
        player_1.cards_count_info()
        player_2.own_cards.append(BJ_deck.cards.pop())
        player_2.own_cards.append(BJ_deck.cards.pop())
        player_2.own_cards_info()
        player_2.cards_count_info()

        if player_1.cards_count() == 21:
            player_1.score_up()
            print(f'В этом раунде победил {player_1.name}!')
            break
        elif player_2.cards_count() == 21:
            player_2.score_up()
            print(f'В этом раунде победил {player_2.name}!')
            break
        else:
            while True:
                ask_for_player_1 = input(f'{player_1.name}, еще карту? Если да - "1", если нет - "0": ')
                if ask_for_player_1 == '0':
                    player_1.cards_count_info()
                    break
                elif ask_for_player_1 == '1':
                    player_1.own_cards.append(BJ_deck.cards.pop())
                    player_1.own_cards_info()
                    player_1.cards_count_info()
                    if player_1.cards_count() == 21:
                        player_1.score_up()
                        print(f'В этом раунде победил {player_1.name}!')
                        break
                    elif player_1.cards_count() > 21:
                        player_2.score_up()
                        print(f'В этом раунде победил {player_2.name}!')
                        break

            while True:
                if player_1.cards_count() >= 21:
                    break
                else:
                    ask_for_player_2 = input(f'{player_2.name}, еще карту? Если да - "1", если нет - "0":')
                    if ask_for_player_2 == '0':
                        print(f'{player_2.name} не хочет рисковать. ')
                        player_2.cards_count()
                        break
                    elif ask_for_player_2 == '1':
                        player_2.own_cards.append(BJ_deck.cards.pop())
                        player_2.own_cards_info()
                        player_2.cards_count_info()
                        if player_2.cards_count() == 21:
                            player_2.score_up()
                            print(f'В этом раунде победил {player_2.name}!')
                            break
                        elif player_2.cards_count() > 21:
                            player_1.score_up()
                            print(f'В этом раунде победил {player_1.name}!')
                            break

            if player_2.cards_count() == player_1.cards_count():
                print(f'В этом раунде ничья!')
            elif 21 >= player_2.cards_count() > player_1.cards_count():
                print(f'В этом раунде победил {player_2.name}!')
            elif 21 >= player_1.cards_count() > player_2.cards_count():
                print(f'В этом раунде победил {player_1.name}!')
    else:
        print('Ошибка ввода. Вводить надо "1" или "0"')