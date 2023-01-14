result = 0

with open('calc.txt', 'r') as text_file:
    for i_line in text_file.readlines():
        try:
            result += eval(i_line)
        except:
            if input(f'Ошибка в строке ({i_line[:-1]}). Исправить? ') == 'да':
                right_string = input('Введите исправленную строку: ')
                result += eval(right_string)
            else:
                pass

print(f'Сумма результатов: {result}')
