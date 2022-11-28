print('Количество стран', end=': ')
country_count = int(input())
countries = dict()
for i in range(2):
    print('{0} страна'.format(i + 1), end=': ')
    cities = input()
    countries_data = cities.split()
    countries[countries_data[0]] = []
    for citi in countries_data[1:]:
        countries[countries_data[0]].append(citi)

for i in range(3):
    print(i + 1, '-й город', end=': ')
    new_citi = input()
    if new_citi in countries.values():
        print('Город {0} расположен в стране'.format(new_citi))
    else:
        print('Города {0} в списке нет'.format(new_citi))
print(countries.values())
print(countries)
