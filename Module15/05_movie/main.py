films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
count_films = int(input('Сколько фильмов хотите добавить? '))
to_watch = []
for _ in range(count_films):
    choose_film = input('Введите название ')
    count = 0
    for i in films:
        if i == choose_film:
            to_watch.append(i)
            break
        else:
            count += 1
        if count == len(films):
            print('Ошибка фильма ', choose_film, 'у нас нет :(')
print('Ваш список любимых фильмов: ', ', '.join(to_watch))
