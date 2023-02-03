def subsequence_q(q):
    if not q == [1, 1]:
        print('Передано неверное значение!')
    else:
        my_list = q[:]
        while True:
            try:
                q = my_list[-my_list[-1]] + my_list[-my_list[-2]]
                my_list.append(q)
                yield q
            except IndexError:
                return


for i, number in enumerate(subsequence_q([1, 1])):
    if i <= 30:
        print(number)
    else:
        break
