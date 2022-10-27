def streamline():
    for _ in range (count_numm-1):
        for i in range(count_numm-1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list
count_numm = int(input('Сколько чисел в списке: '))
my_list = []
for _ in range(count_numm):
    number = input('Введите число: ')
    my_list.append(number)
print(my_list)

print(streamline())
