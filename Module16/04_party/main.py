guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guest = 0
while guest != 'пора спать':
    print('Сейчас на вечеринке', len(guests), 'человек', guests)
    guest = input('Гость пришел или ушел?: ')
    if guest == 'пришел':
        name = input('Имя гостя: ')
        guests.append(name)
    elif guest == 'ушел':
        name = input('Имя гостя: ')
        guests.remove(name)
print('Вечеринка закончилась, все легли спать')
