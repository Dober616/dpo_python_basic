def number(x):
    count = 0
    a = x // 1000 % 10
    b = x // 100 % 10
    c = x // 10 % 10
    d = x // 1 % 10
    for digit in [a, b, c, d]:
        for numm in [a, b, c, d]:
            if digit == numm:
                count += 1
            else:
                count = count
        if count >= 3:
            break
        else:
            break
    return count


first_numm = int(input('Введите первое число: '))
last_numm = int(input('Введите второе число: '))
for x in range(first_numm, last_numm):
    if number(x) >= 3:
        print (x)