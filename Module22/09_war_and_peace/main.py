import os.path
import zipfile

war_zip = zipfile.ZipFile(os.path.abspath('voyna-i-mir.zip'))
war_zip.extract('voyna-i-mir.txt', os.path.abspath(os.path.join('..', '09_war_and_peace')))
war_file = open('voyna-i-mir.txt', 'r')
result = open(os.path.abspath('result_file.txt'), 'w')

alfabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alfabet_lat ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
letter_dict = {}
sorted_dict = {}
for string in war_file:
    for letter in string:
        if letter in alfabet_rus or letter in alfabet_lat:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
sorted_values = sorted(letter_dict.values(), reverse=True)
for i in sorted_values:
    for y in letter_dict.keys():
        if letter_dict[y] == i:
            sorted_dict[y] = letter_dict[y]
            result.write(f'{y}: {sorted_dict[y]}\n')
print(sorted_dict)
war_file.close()
result.close()
