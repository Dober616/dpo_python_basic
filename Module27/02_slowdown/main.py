import time
import functools


def time_freeze(funk):
    @functools.wraps(funk)
    def wrapped_func(*args, **kwargs):
        print(f'Выполняется {funk.__name__}')
        time.sleep(5)
        result = funk(*args, **kwargs)
        return result
    return wrapped_func


@time_freeze
def page_refresh(site_name):
    print(f'Страница сайта {site_name} обновлена')


my_page = page_refresh('VK.com')
