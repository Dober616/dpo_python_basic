

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

temp_list = []
def clean_list(some_list, temp_list):

    for element in some_list:
        if not isinstance(element, list):
            temp_list.append(element)
        else:
            clean_list(element, temp_list)


clean_list(nice_list, temp_list)
print(temp_list)
