

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def clean_list(some_list):
    temp_list = []
    for element in some_list:
        if isinstance(element, list):
            temp_list.append(clean_list(element))
        else:
            temp_list.append(element)
    return temp_list
    # return [element if isinstance(element, int) else clean_list(element) for element in some_list ]

print(clean_list(nice_list))