import os


def find_file_path(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if os.path.join(dirpath, file):
                yield os.path.join(dirpath, file)
            else:
                find_file_path(file)

path = '/Users/druz_kirill/PycharmProjects/dpo_python_basic/Module14'
for i in find_file_path(path):
    print(i)
