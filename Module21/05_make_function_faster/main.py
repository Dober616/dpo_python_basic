def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result

# TODO оптимизировать функцию
my_number = 5
print(calculating_math_func(my_number))

def new_function(data):
    if data == 1:
        return 1
    return data * (new_function(data - 1))

print((new_function(my_number) / my_number ** 3) ** 10)

