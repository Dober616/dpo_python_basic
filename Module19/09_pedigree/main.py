def relative_count(name):
    if name not in family_tree.keys():
        return 0
    else:
        parent = family_tree[name]
        if parent in result:
            count = result[parent] + 1
            return count
        else:
            count = relative_count(parent) + 1
        result[name] = count
        return count

people_count = int(input('Введите количество человек: '))
family_tree = dict()
for i in range(people_count):
    child, parent = input(f'{i + 1} пара: ').split()
    family_tree[child] = parent
family_list = set(family_tree.keys()|family_tree.values())
result = dict()
for name in family_list:
    if name not in result:
        result[name] = relative_count(name)

print('"Высота" каждого члена семьи: ')
for name in sorted(result):
    print(name, result[name])
