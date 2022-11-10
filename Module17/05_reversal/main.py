line = input('Введите строку: ')
cut_line = line[line.index('h')+1::]
reverse_line = cut_line[cut_line.index('h')-1::-1]
print(reverse_line)
