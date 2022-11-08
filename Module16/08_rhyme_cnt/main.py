def list_remove():
    people_round.pop(drop_number - 1)
    return people_round

people_count = int(input('Количество человек: '))
count_number = int(input('Какое число в считалке: '))
people_round = []
print('Значит выбывает каждый', count_number, '- й человек', '\n++++++++++++++++++++++++++++++++++++')
for i in range(1, people_count+1):
    people_round.append(i)
print(people_round)

start_index = 0

while len(people_round) != 1:
    print('Текущий круг: ', people_round)
    drop_number = start_index + count_number
    while drop_number > len(people_round):
        drop_number -= len(people_round)
    print('Начало счета с номера: ', people_round[start_index])
    print('Выбывает человек под номером: ', people_round[drop_number - 1])
    print('=================================')
    list_remove()

    if drop_number == len(people_round):
        start_index = 0
    elif drop_number > len(people_round):
        start_index = len(people_round) - (drop_number - 1)
    else:
        start_index = drop_number-1

print('Остался человек под номером: ', people_round[0])


