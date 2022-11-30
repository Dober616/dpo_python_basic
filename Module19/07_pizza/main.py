count_orders = 3  # int(input('Введите количество заказов: '))
client = dict()

for i in range(count_orders):
    pizza = dict()
    order = input(f'{i + 1} заказ: ').split()
    pizza[order[1]] = order[2]
    if order[0] not in client.keys():
        client[order[0]] = pizza
    else:
        if pizza != order[1]:
            client[order[0]].update(pizza)
        else:
            !!!client[pizza] = client[pizza] + order[2]!!!

            # как бы это блять сложить что-то скорее всего с .pop



for i in client:
    print(i, client[i])
print(client.values())