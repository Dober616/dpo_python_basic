def top_cards(x):
    max = 0
    for i in x:
        if i > max:
            max = i
    return (max)
cards_count = int(input('Количество видеокарт: '))
cards_list = []
last_list = []
for _ in range (cards_count):
    model = int(input('Видеокарта: '))
    cards_list.append(model)
top = top_cards(cards_list)
for i in cards_list:
    if i != top:
        last_list.append(i)
print('Старый список видеокарт: ', cards_list)
print('Новый список видеокарт: ', last_list)
