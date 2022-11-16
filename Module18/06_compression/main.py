import itertools
string = input('Введите строку: ')
new_string = []

for litter, group in itertools.groupby(string):
    new_string.append(litter)
    new_string.append(str([i for i in group].count(litter)))

print(''.join(new_string))
