class File:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print('Такого файла нет, создаем новый')
            self.file = open(self.filename, 'w')
            self.file.write('Файла не было, поэтому создали новый, теперь можете делать с ним что хотите')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

with File('mmm.txt', 'r') as ttt:
   for i in ttt:
       print(i)



