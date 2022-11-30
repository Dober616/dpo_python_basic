def count_count(dictionary):
    result = 0
    for each_list in dictionary:
        result += each_list['quantity']
    return result


def count_prices(dictionary):
    result = 0
    for each_list in dictionary:
        result += each_list['price'] * each_list['quantity']
    return result


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for i in goods:
    print(f'{i} - {count_count(store[goods[i]])} штук, стоимость {count_prices(store[goods[i]])} рубля')
