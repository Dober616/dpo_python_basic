def add_contact():
    abonent = dict()
    name = tuple(input('Введите имя и фамилию через пробел: ').split())

    if name in phonebook.keys():
        print('Такой человек уже есть в контактах')
        return abonent
    else:
        phone_number = int(input('Номер телефона: '))
        abonent[name] = phone_number
        return abonent


def search_name():
    surname_list = dict()
    for i in phonebook.keys():
        if abonent_surname in i:
            surname_list[i] = phonebook[i]
    return surname_list


phonebook = dict()
while True:
    print('Введите номер действия: \n1. Добавить контакт\n2. Найти человека')
    action = int(input())
    if action == 1:
        phonebook.update(add_contact())
        print('Текущий словарь контактов: ', phonebook)
    elif action == 2:
        abonent_surname = input('Введите фамилию для поиска: ')
        for i in search_name():
            print(f'{i}: {search_name()[i]}')

    elif action == 0:
        break
