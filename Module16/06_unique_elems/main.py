def numm_remove(my_list):
    my_list.remove(x)
    return my_list


first_list = []
sec_list = []
for i in range(3):
    print('Введите', i+1, 'число для первого списка: ', end='')
    number = int(input())
    first_list.append(number)
for i in range(7):
    print('Введите', i+1, 'число для второго списка: ', end='')
    number = int(input())
    sec_list.append(number)
print(first_list)
print(sec_list)

first_list.extend(sec_list)
print(first_list)
for i in first_list:
    x = first_list.count(i)
    for _ in range(x - 1):
        first_list.remove(i)
print('Новый список с уникальными элементами: ', first_list)
