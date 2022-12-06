my_string = input('Введите строку: ')
mono_litters = set()
for letter in my_string:
    if letter in mono_litters:
        mono_litters.remove(letter)
    else:
        mono_litters.add(letter)
if len(mono_litters) > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')