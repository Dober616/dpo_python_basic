def streamline():
    for i in my_list:
        for y in my_list:
            if i > y:
                my_list.insert(len(my_list)-1, i)
    return my_list
count_numm = int(input('Сколько чисел в списке: '))
my_list = []
for _ in range(count_numm):
    number = int(input('Введите число: '))
    my_list.append(number)
print(my_list)

print(streamline())
