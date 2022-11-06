def drop_numm():
    number = numm_index + (count_number - 1) - len(people_round)
    while number > len(people_round):
        number -= len(people_round)
    return number

people_count = 5  # int(input('Количество человек: '))
count_number = 7  # int(input('Какое число в считалке: '))
people_round = []
print('Значит выбывает каждый', count_number, '- й человек', '\n++++++++++++++++++++++++++++++++++++')
for i in range(1, people_count+1):
    people_round.append(i)

numm_index = 0
while len(people_round) != 1:
    print('Текущий круг людей: ', people_round)
    print('Начало счета с номера: ', people_round[drop_numm()-1])
    if drop_numm() > len(people_round):
        numm_index = drop_numm()-len(people_round)
    else:
        numm_index = drop_numm()
    print('Выбывает номер: ', drop_numm())
    print()
    people_round.pop(drop_numm()-1)
print('Остался человек под номером: ', people_round[0])
