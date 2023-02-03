import os
def gen_file_path(folder, path):
    if not path:
        path = os.path.abspath(os.path.join(os.path.sep))
        for i in os.listdir(path):
            temp = os.path.abspath(os.path.join(path, i))
            if os.path.isdir(temp) and i != folder:
                gen_file_path(folder, path)
            yield temp
            if i == folder:
                return


ttt = gen_file_path(work, 'main.py')