n_count = int(input('Количество стран: '))
country_cities = dict()
for i in range(n_count):
    names = input(f'Введите {i+1}-ю страну и города: ').split()
    country_cities[names[0]] = []
    for city in names[1:]:
        country_cities[names[0]].append(city)
for i in range(1, 4):
    new_city = input(f'{i}-й город: ')
    for key in country_cities:
        if new_city in country_cities[key]:
            print(f'Город {new_city} расположен в стране {key}')