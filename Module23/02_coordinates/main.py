import random

coord_count = int(input('Количество координат: '))

with open('coordinates.txt', 'w') as w_coordinates:
    for _ in range(coord_count):
        w_coordinates.write(str(f'{random.randint(10, 20)} {random.randint(10, 20)}\n'))


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        with open('result.txt', 'w') as file_2:
            for line in file:
                nums_list = line.split()
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                try:
                    res2 = f2(int(nums_list[0]), int(nums_list[1]))
                    try:
                        number = random.randint(0, 100)
                        my_list = sorted([res1, res2, number])
                        file_2.write(str(f'{my_list[0]} {my_list[1]} {my_list[2]}\n'))
                    except Exception:
                        print("Что-то пошло не так")
                except Exception:
                    print("Что-то пошло не так со второй функцией")

except Exception:
    print("Что-то пошло не так с первой функцией")
