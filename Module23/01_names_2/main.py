len_summ = 0
string_count = 0
try:
    with open('people.txt', 'r') as people_file:
        for name in people_file:
            string_count += 1
            lenght = len(name)
            if name.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                raise BaseException
            len_summ += lenght
except FileNotFoundError:
    print('Такой файл не найден.')
except BaseException:
    print(f'Длина строки {string_count} меньше 3 букв')
finally:
    print(f'Итоговая сумма символов: {len_summ}')
