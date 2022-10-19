def separation1(number):
    parts = str(number).split(".")[::-1]
    first_part = int(parts[1])
    return first_part
def separation2(number):
    parts = str(number).split(".")[::-1]
    sec_part = int(parts[0])
    return sec_part
def reverse(number):
    rev_numm = 0
    while number != 0:
        digit = number % 10
        rev_numm *= 10
        rev_numm += digit
        number //= 10
    return rev_numm
def reverse2(number):
    rev_numm = 0
    count = 0
    while number != 0:
        digit = number % 10
        rev_numm *= 10
        rev_numm += digit
        number //= 10
        count += 1
    return round(rev_numm * 10 ** -count, count)
first_numm = float(input('Введите первое вещественное число: '))
sec_numm = float(input('Введите второе вещественное число: '))
first_part1 = separation1(first_numm)
sec_part2 = separation2(first_numm)
a = (reverse(separation1(first_numm))+(reverse2(separation2(first_numm))))
b = (reverse(separation1(sec_numm))+(reverse2(separation2(sec_numm))))
print('Первое число наоборот = ', a)
print('Второе число наоборот = ', b)
print('Сумма: ', a + b)




