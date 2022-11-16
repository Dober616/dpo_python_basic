password = input('Придумайте пароль: ')
if len(password) < 8:
    print('Пароль слишком короткий')
elif sum(map(str.isupper, password)) < 1:
    print('Мало заглавных букв')
elif sum(map(str.isalnum, password)) < 3:
    print('Нужно хотя бы 3 цифры')
else:
    print('Это надежный пароль!')
