# def drop_numm():
#     number = remove_index + (count_number - 1) - len(people_round)
#     while number > len(people_round):
#         number -= len(people_round)
#     return number

# people_count = 5  # int(input('Количество человек: '))
count_number = 7  # int(input('Какое число в считалке: '))
people_round = ['a', 'b', 'c', 'd', 'e']
# people_round = []
print('Значит выбывает каждый', count_number, '- й человек', '\n++++++++++++++++++++++++++++++++++++')
# for i in range(1, people_count+1):
#     people_round.append(i)
# print(people_round)


start_index = 0

while len(people_round) != 1:
    print('Текущий круг: ', people_round)
    print('Начало счета с номера: ', people_round[start_index])
    drop_number = start_index + count_number
    while drop_number > len(people_round):
        drop_number -= len(people_round)
    people_round.pop(drop_number-1)
    start_index = drop_number
    print('Выбывает человек под номером: ', people_round[drop_number-1])

