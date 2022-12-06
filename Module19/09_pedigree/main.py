def relative_count(name):

    if name not in family_tree:
        result[name] = 0
        return 0
    parent = family_tree[name]
    if parent in result:
        count = result[parent] + 1
    else:
        count = relative_count(parent) + 1
        result[name] = count
        return count

people_count = int(input('Введите количество человек: '))
family_tree = dict()
for i in range(people_count):
    child, parent = input('Введите ребенка и родителя: ').split()
    family_tree[child] = parent

family_list = set(family_tree.keys()|family_tree.values())
result = dict()
for name in family_list:
    if name not in result:
        relative_count(name)
print(result)

# for name in sorted(result):
#     print('Высота каждого члена семьи: \n', name, result[name])
