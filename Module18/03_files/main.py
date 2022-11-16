forbidden_symbols = '@№$%^&\*()'
allowed_formats = '.txt .docx'
file_name = input('Введите название файла: ')

if file_name.startswith(tuple(forbidden_symbols)) == True:
    print('Ошибка: навание начинается на один из запрещенных символов.')
elif file_name.endswith(tuple(allowed_formats)) == False:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно')

