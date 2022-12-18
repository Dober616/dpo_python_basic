def subsequence_nums(number):
    if number == 0:
        return 1
    subsequence_nums(number - 1)
    print(number)


number = 10

subsequence_nums(number)

