initial_file = open('numbers.txt', 'r')
data = initial_file.read()
numbers_list = []
for line in data:
    for symbol in line:
        if symbol.isdigit():
            numbers_list.append(symbol)
result = 0
for digit in numbers_list:
    result += int(digit)

final_data = open('answer.txt', 'w')
final_data.write(str(result))
initial_file.close()
final_data.close()