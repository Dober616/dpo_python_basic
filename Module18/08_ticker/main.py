def new_string(temp_string, i):
    temp = temp_string[i:len(temp_string) + 1] + temp_string[0:i]
    return temp
first_string = 'abcd'
second_string = 'cdab'
shift = 0
for i in range(4):
    if first_string == new_string(second_string, i):
        print('Первая строка получается из второй со сдвигом', shift)
    else:
        shift += 1
