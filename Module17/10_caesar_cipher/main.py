text = input('Введите сообщение: ')
alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
shift = int(input('Введите сдвиг: '))
encrypted_message = [alfabet[alfabet.index(letter) - len(alfabet) + shift] if letter in alfabet else letter for letter in text]

print(''.join(encrypted_message))
# В общем как-то так получилось...
