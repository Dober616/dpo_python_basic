def streamline():
    for _ in range (count_numm):
        for i in my_list:
            for y in my_list:
                if i > y:
                    my_list.insert(y, i)
                    my_list.remove(i)
                elif i <= y:
                    my_list.insert(i, y)
                    my_list.remove(y)
    return my_list

count_numm = int(input('Сколько чисел в списке: '))
my_list = []
for _ in range(count_numm):
    number = int(input('Введите число: '))
    my_list.append(number)
print(my_list)


print(streamline())
