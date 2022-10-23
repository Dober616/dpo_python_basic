cells_efficency = []
bad_cells = []
sells_count = int(input('Количество клеток: '))
for i in range (sells_count):
    print('Эффективность ', i+1, 'клетки: ', end='')
    efficency = int(input())
    cells_efficency.append(efficency)
for cell in  cells_efficency:
    if cells_efficency.index(cell) + 1 > cell:
        bad_cells.append(cell)
print('Количество клеток: ', len(cells_efficency))
print('Неподходящие значения: ', bad_cells)