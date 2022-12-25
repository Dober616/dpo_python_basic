def towers(n, first, last):
    if n == 0:
        return
    temp = 6 - first - last
    towers(n - 1, first, temp)
    print(f'Перенести диск {n} со стержня {first} на стержень {last}')
    towers(n - 1, temp, last)

towers(3, 1, 3)