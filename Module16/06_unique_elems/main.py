first_list = [1, 2, 3]
sec_list = [2, 4, 6, 3, 3, 2, 1]
new_list = []
# for i in range(3):
#     print('Введите', i+1, 'число для первого списка: ', end='')
#     number = int(input())
#     first_list.append(number)
# for i in range(7):
#     print('Введите', i+1, 'число для второго списка: ', end='')
#     number = int(input())
#     sec_list.append(number)
first_list.extend(sec_list)
new_list.extend(first_list)
print('Первый лист', first_list)
for number in first_list:
    for i in new_list:
        if i == number:
            first_list.remove(number)
            break
        new_list.remove(i)
print('Новый список с уникальными эелементами:', first_list)
