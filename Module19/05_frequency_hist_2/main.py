def dictionary():
    for symb in text:
        if symb not in symb_list:
            symb_list[symb] = 1
        else:
            symb_list[symb] += 1
    return symb_list


symb_list = dict()
text = input('Введите текст: ')
symb_list.update(dictionary())
new_dict = dict()
print(f'Оригинальный словарь частот: ')
for key in symb_list.keys():
    print(f'{key}: {symb_list[key]}')
print('Инвертированный словарь частот: ')

for i in set(symb_list.values()):
    new_dict[i] = []
for letter in symb_list.keys():
    new_dict[symb_list[letter]].append(letter)
for count in new_dict:
    print(f'{count}: {new_dict[count]}')
