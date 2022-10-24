def cont_place():
    for i in containers_area:
        if new_container >= i:
            break
    return i
container_count = int(input('Введите количество контейнеров: '))
containers_area = []
for _ in range (container_count):
    mass_cont = int(input('Введите вес контейнера: '))
    while mass_cont > 200:
        print('Ошибка! Вес конейнера не может превышать 200')
        mass_cont = int(input('Введите вес контейнера: '))
    containers_area.append(mass_cont)
print(containers_area)
new_container = int(input('Введите вес нового контейнера: '))
while new_container > 200:
    print('Ошибка! Вес конейнера не может превышать 200')
    new_container = int(input('Введите вес контейнера: '))
if cont_place() != len(containers_area):
    containers_area.insert(containers_area.index(cont_place()), new_container)
else:
    containers_area.append(new_container)
print(containers_area)
print('Номер, который получит новый контейнер: ', containers_area.index(new_container)+1)

