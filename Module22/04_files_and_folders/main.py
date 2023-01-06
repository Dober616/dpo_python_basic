import os


def files_n_dirs(path):
    files = 0
    dirs = 0
    files_size = 0
    for element in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, element))):
            file_path = os.path.abspath(os.path.join(path, element))
            files_size += os.path.getsize(file_path)
            files += 1
        else:
            result = files_n_dirs(os.path.abspath(os.path.join(path, element)))
            files += result[0]
            dirs += 1
    return files, dirs, files_size


my_path = os.path.abspath(os.path.join('..', '..', 'Module22'))

print(f'Количество файлов: {files_n_dirs(my_path)[0]}')
print(f'Количество папок: {files_n_dirs(my_path)[1]}')
print(f'Размер папки: {files_n_dirs(my_path)[2]//1024} КБ')




