import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


site_count = int(input('Сколько сайтов: '))


def change_product(site):
    for _ in range(site_count):
        product_name = input('Введите название продукта для нового сайта: ')
        print(f'Сайт для {product_name}')
        duplicate_site = copy.deepcopy(site)
        duplicate_site['html']['head']['title'] = f'Куплю/продам {product_name} недорого'
        duplicate_site['html']['body']['h2'] = f'У нас самая низкая цена на {product_name}'
        print(duplicate_site)


change_product(site)

