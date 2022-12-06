import random
mistery = input('Загадайте число: ')
max_numm = int(input('Введите максимальное число: '))
result = set()
numm_list = set([random.randint(1, max_numm) for _ in range(3)])
question = input(f'Нужное число есть среди вот этих чисел {numm_list}? \nОтвет Артема: ')
while question != 'Помогите':
    numm_list = set([random.randint(1, max_numm) for _ in range(3)])
    question = input(f'Нужное число есть среди вот этих чисел {numm_list}? \nОтвет Артема: ')
    if question == 'да':
        result.update(numm_list)
    else:
        result.difference(numm_list)
print('Артем мог загадать следующие числа: ', set(result))
