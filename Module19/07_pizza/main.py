count_orders = int(input('Введите количество заказов: '))
client = dict()

for i in range(count_orders):
    pizza = dict()
    order = input(f'{i + 1} заказ: ').split()
    pizza[order[1]] = order[2]
    if order[0] not in client.keys():
        client[order[0]] = pizza
    else:
        if order[1] not in client[order[0]]:
            client[order[0]].update(pizza)
        else:
            client[order[0]][order[1]] = int(client[order[0]][order[1]]) + int(order[2])
                # вроде как ошибка но вроде как работает

for i in client:
    print(i, client[i])
