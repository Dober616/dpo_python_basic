list_length = int(input('Введите длину списка: '))

final_list = [(1 if x % 2 == 0 else x % 5) for x in range(1, list_length + 1)]
print(final_list)
