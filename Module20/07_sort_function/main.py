def sort_tupple():
    for numm in my_tupple:
        if not isinstance(numm, int):
            return my_tupple
    return sorted(my_tupple)


my_tupple = 6, 3, -1, 8, 4, 10, -5
print(sort_tupple())
