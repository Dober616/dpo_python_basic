def duti():
    ballance = 0
    for elements in duti_list:
        if elements[0] == friend+1:
            ballance += elements[2]
        elif elements[1] == friend+1:
            ballance -= elements[2]
    return ballance

friends_count = int(input('Количество друзей: '))
duti_resceipt = int(input('Долговых расписок: '))
duti_list = []
temp_list = []
for i in range(duti_resceipt):
    print(i+1, '-ая расписка')
    creditior = int(input('Кому: '))
    temp_list.append(creditior)
    debtor = int(input('От кого: '))
    temp_list.append(debtor)
    how_much = int(input('Сколько: '))
    temp_list.append(how_much)
    duti_list.append(temp_list)
    temp_list = []

print('Баланс друзей: ')
for friend in range(friends_count):
    print(friend+1, ':', duti())

