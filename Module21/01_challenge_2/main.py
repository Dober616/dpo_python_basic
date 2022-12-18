def none_cycle(some_numm):
    if some_numm != 1:
        none_cycle(some_numm - 1)
    print(some_numm)



numm = int(input('Введите num: '))

none_cycle(numm)

