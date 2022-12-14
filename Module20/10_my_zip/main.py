def my_zip():
    result_line = []
    if len(line_1) <= len(line_2):
        short = len(line_1)
    else:
        short = len(line_2)
    for i in range(short):
        temp_tuple = line_1[i], line_2[i]
        result_line.append(temp_tuple)
    return result_line

line_1 = ('abcd')
line_2 = (10, 20, 30, 40)
for i in my_zip():
    print(i)

