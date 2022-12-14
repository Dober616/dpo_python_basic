def last_numm():
    new_list = []
    for index, numm in enumerate(slicer[0]):
        if numm == 2:
            new_list.append(index)
    new_list = tuple(new_list)
    if slicer[0].count(2) > 1:
        return slicer[0][new_list[0]:new_list[1] + 1]
    elif slicer[0].count(2) == 1:
        return slicer[0][new_list[0]:]
    else:
        return ()


slicer = ((1, 3, 4, 5, 2, 6, 7, 8, 9, 2, 10), 2)
print('Ответ в консоли: ', last_numm())
