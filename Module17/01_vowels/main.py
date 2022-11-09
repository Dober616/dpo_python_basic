my_text = input('Введите текст: ')

vowel = 'ауоыиэяюёе'

vowel_list = [x for x in my_text for letter in vowel if x == letter]
print('Список гласных букв: ', vowel_list, '\nДлина списка: ', len(vowel_list))
