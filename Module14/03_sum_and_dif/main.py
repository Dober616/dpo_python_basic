def summ(number):
    summ = 0
    while number != 0:
        gigit = number % 10
        summ += gigit
        number //=10
    return summ
def count(number):
    count = 0
    while number != 0:
        number //=10
        count +=1
    return count

number = int(input('Введите число: '))
print('Сумма цифр: ', summ(number))
print('Количество цифр в числе: ', count(number))
print('Разность суммы и количества цифр: ', summ(number)-count(number))