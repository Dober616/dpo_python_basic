import random
def pairs(origin_list):
    first_list = []
    secnd_list = []
    for i, number in enumerate(origin_list):
        if i % 2 == 0:
            first_list.append(number)
        else:
            secnd_list.append(number)
    return zip(first_list, secnd_list)


origin_list = [random.randint(0, 10) for _ in range(10)]
result_list = []
print('Оригинальный список: ', origin_list)
for i in pairs(origin_list):
    result_list.append(i)
print('Новый список: ', result_list)
