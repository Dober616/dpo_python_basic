def min_len(len_1, len_2):
    return min(len(len_1), len(len_2))


def my_zip(data_1, data_2):
    new_tupple = ((data_1[i], data_2[i]) for i in range(min_len(my_string, my_tupple)))
    return new_tupple



my_string = 'qwer' # input('Введите строку')
my_tupple = (10, 20, 30, 40) # input('Введите кортеж')

for i in my_zip(my_string, my_tupple):
    print(i)
