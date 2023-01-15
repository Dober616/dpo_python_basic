import random


def is_exeptation_raise():
    return random.randint(1, 13) == 7


summ = 0
with open('out_file.txt', 'w') as result_file:
    while summ < 777:
        numm = int(input('Введите число: '))
        summ += numm
        try:
            if is_exeptation_raise():
                raise Exception
        except Exception:
            print('Сегодня не ваш день')
        result_file.write(f'{str(numm)}\n')
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
