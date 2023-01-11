import os

letters = {}
letters_frequency = {}
alfabet = 'abcdefghijklmnopqrstuvwxyz'
original_file = open(os.path.abspath('text.txt'), 'r')
final_file = open(os.path.abspath('analysis.txt'), 'w')
for string in original_file:
    for letter in string:
        if letter.lower() in alfabet:
            if letter.lower() in letters:
                letters[letter.lower()] += 1
            else:
                letters[letter.lower()] = 1

for letter in sorted(letters):
    letters_frequency[letter] = round(letters[letter] / sum(letters.values()), 3)
    letters_frequency = dict(sorted(letters_frequency.items(), key=lambda item: item[1]))
for element in letters_frequency:
    final_file.write(f'{element} {letters_frequency[element]}\n')
original_file.close()
final_file.close()


# никак не могу понять как отсортировать по 2 параметрам
