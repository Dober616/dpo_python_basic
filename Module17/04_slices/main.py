alphabet = 'abcdefg'
print('1. Копия строки: \t\t\t\t', alphabet[:])
print('2. В обратном порядке: \t\t\t', alphabet[::-1])
print('3. Каждый второй элемент: \t\t', alphabet[::2])
print('4. Каждый второй после первого:\t', alphabet[1::2])
print('5. Все элементы до второго: \t', alphabet[:1])
print('6. Все с конца до предпосл.: \t', alphabet[-1:-2:-1])
print('7. В диапаз. от 3 до 4(без 4): \t', alphabet[3:4])
print('8. Последние три элемента : \t', alphabet[:3:-1])
print('9. Все в диапазоне от 3 до 4: \t', alphabet[3:5])
print('10.То же в обратном порядке: \t', alphabet[4:2:-1])
