def count(x, num_list):
    count = 0
    main_list.extend(num_list)
    for number in main_list:
        if number == x:
            count += 1
    return count


def cut(x, num_list):
    main_list.extend(num_list)
    for i in main_list:
        if i == x:
            main_list.remove(i)
    return main_list


main_list = [1, 5, 3]
first_minor_list = [1, 5, 1, 5]
second_minor_list = [1, 3, 1, 5, 3, 3]

print('Количество цифр 5 при первом объединении:', count(5, first_minor_list))
print('Количество цифр 3 при первом объединении:', count(3, second_minor_list))
print('Итоговый список: ', cut(5, first_minor_list))
