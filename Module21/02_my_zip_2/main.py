my_string = [{"x": 4}, "b", "z", "d"]
my_tupple = (10, {20,}, [30], "z")
def new_zip(frst_data, scnd_data, i, my_list=[]):
    if i < 0:
        return 0
    temp_tuple = (frst_data[i], scnd_data[i])
    new_zip(frst_data, scnd_data, i - 1)
    my_list.append(temp_tuple)
    return my_list


tuple_lenght = min(len(my_string), len(my_tupple))-1
print(new_zip(my_string, my_tupple, tuple_lenght))
