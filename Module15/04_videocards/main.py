def top_cards(x):
    max = 0
    for i in x:
        if i > max:
            max = i
    return (max)
cards_count = int(input('Введите количество видеокарт: '))
print('Количество видеокарт: ', cards_count)
cards_list = []
for _ in range (cards_count):
    model = int(input('Видеокарта: '))
    cards_list.append(model)
cards_list.remove(top_cards(cards_list))
print(cards_list)

#Не совсем понятно, сколько последних карт удалять. 
