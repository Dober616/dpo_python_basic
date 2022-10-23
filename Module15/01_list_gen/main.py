numbers_list = []
number = int(input('До какого числа: '))
for i in range (1, number+1, 2):
    numbers_list.append(i)
print('Список из нечетных чисел от 1 до ', 'N', ':', numbers_list)
