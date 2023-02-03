# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break



list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
def refactoring():
    for x in list_1:
        for y in list_2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == to_find:
                print('Вы нашли!!!')
                return

for i in refactoring():
    print(i)