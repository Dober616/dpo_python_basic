def is_prime(numm):
    for i in range(2, numm + 1):
        res = numm % i
        if res == 0:
            if i == numm:
                return True
            else:
                return False

my_list = 'О дивный новый мир!'
new_list = []
for index, numm in enumerate(my_list):
    if is_prime(index):
        new_list.append(numm)
print(new_list)