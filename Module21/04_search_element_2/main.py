def find_key(data, some_key, depth=None):
    if depth == 0:
        return None
    if some_key in data:
        return data[some_key]
    for sub_data in data.values():
        if isinstance(sub_data, dict):
            if depth:
                result = find_key(sub_data, my_key, depth - 1)
                if result:
                    break
            else:
                result = find_key(sub_data, my_key)
                if result:
                    break
    else:
        return None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, навеное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

my_key = input('Введите искомый ключ: ')
question_depth = input('Хотите ввести максимальную глубину?(да/нет): ')
if question_depth.lower() == 'да':
    max_depth = int(input('Введите максимальную глубину: '))
    if find_key(site, my_key, max_depth):
        print(find_key(site, my_key, max_depth))
    else:
        print('Искомый ключ не найден')
else:
    if find_key(site, my_key):
        print(find_key(site, my_key))
    else:
        print('Искомый ключ не найден')
