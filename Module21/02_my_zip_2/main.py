def my_zip_2(*args):
    min_len = min(list((len(data) for data in args)))
    return [tuple(list(element)[index] for element in args) for index in range(min_len)]


a = [1, 2, 3, 4, 5]
b = {1: "s", 2: "q", 3: 4}
x = (1, 2, 3, 4, 5)

print(my_zip_2(a, b, x))

# только вот без циклов с аргами не получается