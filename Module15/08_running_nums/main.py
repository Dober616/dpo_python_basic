def table(my_list):
    for _ in range (move):
        my_list = my_list[1:]+my_list[:1]
    return my_list
my_list = []
new_list = []
count_numbers = int(input('Введите количество элементов списка: '))
for _ in range(count_numbers):
    number = input('Введите число: ')
    my_list.append(number)
move = int(input('Сдвиг: '))
print(my_list)
print(table(my_list))
