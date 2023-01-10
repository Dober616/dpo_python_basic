initial_file = open('numbers.txt', 'r')
data = initial_file.read()
final_data = open('answer.txt', 'w')
summ = 0
for line in data.split('\n'):
    for sym in line.split(' '):
        if sym.isdigit():
            summ += int(sym)

final_data.write(str(summ))
initial_file.close()
final_data.close()