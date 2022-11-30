couples_words = int(input('Введите количество пар слов: '))
sinonim_dict = dict()
for i in range(couples_words):
    word = input(f'{i + 1}-я пара: ').split(' - ')
    sinonim_dict[word[0]] = word[1]

print(sinonim_dict.up)
my_word = input('Введите слово: ')
if my_word in sinonim_dict.keys():
    print(f'Синоним слова {my_word}: {sinonim_dict[my_word]}')
else:
    while my_word not in sinonim_dict.keys():
        my_word = input('Такого слова нет \nВведите другое: ')
    print(f'Синоним слова {my_word}: {sinonim_dict[my_word]}')

# Завис на проверке без учета регистра. Не могу найти как уменьшить все буквы в справочнике