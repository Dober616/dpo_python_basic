def new_function(data):
    if data == 1:
        return 1
    return data * (new_function(data - 1))


my_number = 5
print((new_function(my_number) / my_number ** 3) ** 10)
