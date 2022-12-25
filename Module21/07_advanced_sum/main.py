def list_sum(my_list):
    return sum(element if isinstance(element, int) else list_sum(element) for element in my_list)


print(list_sum([1, 2, 3, [1, 2, [3, 4]]]))
