import os


data = open(os.path.abspath('text.txt'), 'w')
for i in range(4):
    data.write('Hello\n')
data.close()
alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
read_data = open(os.path.abspath('text.txt'), 'r')
write_data = open(os.path.abspath('cipher_text.txt'), 'w')
shift = 1
for string in read_data:
    encrypted_string = [alfabet[alfabet.index(letter) - len(alfabet) + shift] if letter in alfabet else letter for letter in string]
    write_data.write(''.join(encrypted_string))
    shift += 1

read_data.close()
write_data.close()

