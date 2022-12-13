import random

player_list = ['Jack', 'Alex', 'Max']
entryes_count = int(input('Сколько записей вносится в протокол? '))
game_dict = dict()
print('Записи (результат и имя):')
for i in range(entryes_count):
    game_dict[f'{i + 1}'] = (random.randint(0, 999999), random.choice(player_list))

for i_string in game_dict:
    print(f'{i_string}-я запись: {game_dict[i_string]}')
winners = []
for result in sorted((game_dict.values()), reverse=True):
    winners.append(result)


winners_dict = dict()
for i in range(len(winners)):
    if winners[i][1] not in winners_dict:
        winners_dict[winners[i][1]] = winners[i][0]
print()
print('Итоги соревнований: ')
count = 1
for player in winners_dict:
    print(f'{count}-е место. {player} ({winners_dict[player]})')
    count += 1
