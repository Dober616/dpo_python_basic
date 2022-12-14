def min_len():
    return min(len(my_string), len(my_tupple))

my_string = 'qwer'
my_tupple = (10, 20, 30, 40)

new_tupple = ((my_string[i], my_tupple[i]) for i in range(min_len()))
for i in new_tupple:
    print(i)
