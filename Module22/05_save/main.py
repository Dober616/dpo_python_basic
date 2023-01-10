import os


my_text = input('Введите строку: ')
my_path = ' ' + input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
file_name = input('Введите имя файла: ')
dir_path = os.path.join(my_path.replace(' ', '/'))
file_path = os.path.join(dir_path, file_name)
check_file = os.path.exists(file_path)
if not check_file:
    data = open(file_path, 'w')
    data.write(my_text)
    data.close()
    print(f'Файл {file_name} успешно сохранен')
else:
    question = input('Такой файл уже существует. Вы действительно хотите перезаписать файл? (y/n): ')
    if question == 'y':
        data = open(file_path, 'w')
        data.write(my_text)
        data.close()
        print('Данные успешно перезаписаны')
    else:
        print('Ну тогда ничего делать не будем')

# здесь немного заколхозил с началом пути для папки,
# #так как на маке путь начинается со слеша




