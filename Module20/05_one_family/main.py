family_dict = {
    'Кирилл Друзьяк': 38,
    'Катя Друзьяк': 33,
    'Аня Романова': 34,
    'Сергей Витолс': 35,
    'Вадим Романов': 40,
    'Олег Друзьяк': 60,
    'Николай Виноградов': 83,
}

age_list = []
some_surname = input('Введите фамилию: ')
for name in family_dict.keys():
    if some_surname.lower() in name.lower():
        age_list.append(name)

for i in age_list:
    print(i, family_dict[i])

