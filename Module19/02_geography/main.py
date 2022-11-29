def citi_search():
    for country in result:
        if citi in result[country]:
            return country
    return False


count = int(input('Количество стран: '))
result = dict()
for i in range(count):
    data = input(f'{i+1}-я страна: ').split()
    result[data[0]] = []
    for j in data[1:]:
        result[data[0]].append(j)

for attemp in range(3):
    citi = input(f'{attemp + 1}-й город: ')
    if citi_search():
        print(f'Город {citi} расположен в стране в {citi_search()}')
    else:
        print(f'По городу {citi} данных нет')


