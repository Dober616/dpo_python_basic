n = int(input('Количество чисел: '))
numm_in_list = int(input('Сколько чисел в посдсписке: '))
my_list = [[number for number in range(i, n + 1, n // numm_in_list)]
           for i in range(1, n // numm_in_list + 1)]
print('Двуменрый список: ', my_list)
