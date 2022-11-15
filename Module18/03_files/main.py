forbidden_symbols = '@№$%^&\*()'.split(',')
allowed_formats = '.txt, .docx'
file_name = input('Введите название файла: ')
if file_name.startswith():
    print('Внимание, запрещенные символы!')
elif file_name.endswith(allowed_formats):
    print('Внимание, запрещенный формат')
else:
    print('Все ок')
