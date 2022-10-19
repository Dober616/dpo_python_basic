def gsd(number):
    for i in range (2, number+1):
        if number % i == 0:
            gsd = i
            break
    return gsd
number = int(input('Введите число: '))
if number <= 1:
    number = int(input('Число должно быть больше 1. Введите число повторно: '))
print(gsd(number))