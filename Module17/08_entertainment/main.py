import random

def rnd():
    left_i = random.randrange(1, stick_count, 1)
    right_i = random.randrange(left_i, stick_count, 1)
    return left_i, right_i


stick_count = int(input('Количество палок: '))
drop_count = int(input('Количество бросков: '))
my_list = []
drop_list = []
for i in range(1, stick_count+1):
    my_list.append(i)

for i in range(drop_count):
    Left_i, Right_i = rnd()
    print('Бросок ', i + 1)
    for stick in range(Left_i, Right_i + 1):
        drop_list.append(stick)
    print('Сбиты палки с номера ', Left_i, 'по номер ', Right_i)
new_list = ['.' if i in drop_list else 'I' for i in my_list]

print('Результат: ', ' '.join(new_list))
