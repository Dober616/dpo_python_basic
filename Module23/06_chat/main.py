from datetime import datetime
while True:
    action = int(input(
                   '0 - Посмотреть текущий текст чата\n'
                   '1 - Отправить сообщение\n'
                   'Выберите действие: '))
    if action == 0:
        try:
            with open('chat_ru.txt', 'r') as chat_r:
                for line in chat_r:
                    print(line)
        except FileNotFoundError:
            print('Такой чат не найден')
    elif action == 1:
        name = input('Введите имя пользователя: ')
        message = input('Введите сообщение: ')
        current_datetime = datetime.now().replace(microsecond=0)
        with open('chat_ru.txt', 'a+') as chat_w:
            chat_w.write(f'\n{current_datetime}\n{name} => {message}')
