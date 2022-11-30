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
print('Инвертированный словарь частот: ')
new_dict = dict()
for i in set(symb_list.values()):
    new_dict[i] = []
for letter in symb_list.keys():
    new_dict[symb_list[letter]].append(letter)
for count in new_dict:
    print(f'{count}: {new_dict[count]}')
