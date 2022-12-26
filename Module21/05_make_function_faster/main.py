def calculating_math_func(data, my_dict=None):
    if data in my_dict:
        return my_dict[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        result /= data ** 3
        result = result ** 10
        my_dict[data] = result
    return result

print(calculating_math_func(5, my_dict=dict()))
