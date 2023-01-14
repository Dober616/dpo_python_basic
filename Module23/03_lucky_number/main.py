summ = 0
with open('out_file.txt', 'w') as result_file:
    while summ < 777:
        numm = int(input('Введите число: '))
        summ += numm
        result_file.write(f'{str(numm)}\n')
    print('Вы успешно выполнили условие для выхода из порочного цикла!')