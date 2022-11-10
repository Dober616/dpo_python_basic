import random
n = int(input('Количество чисел в списке: '))
my_list = [random.randint(0, 2) for _ in range(n)]
cut_list = [numm  for numm in my_list if numm != 0]
reaped_list = cut_list + [0] * (len(my_list) - len(cut_list))

print(my_list)
print(reaped_list)
print(cut_list)
