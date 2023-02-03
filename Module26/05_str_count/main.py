import os


def string_count():
    count = 0
    files = os.listdir()
    for file in  files:
        if file.rstrip('.py'):
            with open(file, 'r') as my_file:
                for line in my_file:
                    count += 1
        print(files)
        return count

print(string_count())
