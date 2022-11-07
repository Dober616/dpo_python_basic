count_numbers = int(input('Количество чисел: '))
subsequence = []
for _ in range(count_numbers):
    number = int(input('Число: '))
    subsequence.append(number)
add_list = []
y = 1
for digit in subsequence:
    last_numm = subsequence[-y]
    if digit == last_numm:
        y += 1
    else:
        add_list.insert(0, digit)
if len(add_list) > 0:
    print('Последовательность: ', subsequence, '\nНужно приписать чисел: ', len(add_list), '\nСами числа: ', add_list)
