main_menu = input('Введите блюда из основного меню: '.split(';'))
print('Доступное меню: ', main_menu)
print('На данный момент в меню есть: ', ', '.join(main_menu.split(';')))
