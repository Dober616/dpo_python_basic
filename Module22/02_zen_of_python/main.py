zen_python = open('zen.txt', 'r')
data = zen_python.read()
final_data = open('result.txt', 'w')
for line in reversed(data.split('\n')):
    final_data.write(f'{line}\n')
zen_python.close()
final_data.close()

