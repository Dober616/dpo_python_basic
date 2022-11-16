my_string = input('Введите строку: ').split()
new_string = [word.capitalize() for word in my_string]
print("Результат: ", ' '.join(new_string))
