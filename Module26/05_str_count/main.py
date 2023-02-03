import os


def strings_count(path):
    all_strings = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if os.path.join(dirpath, file).endswith('.py'):
                curr_file = open(os.path.join(dirpath, file), 'r')
                for line in curr_file.readlines():
                    if not (line == '\n'):
                        all_strings += 1
    return all_strings


print(f'Количество строк кода в модуле: {strings_count("/Users/druz_kirill/PycharmProjects/Module26")}')
