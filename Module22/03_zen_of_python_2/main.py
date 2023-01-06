def letters_count(letters):
    for letter in data:
        if letter.lower() in alfabet:
            letters += 1
    return letters
def words_count(words):
    for word in data.split(' '):
        words += 1
    return words
def strings_count(strings):
    for string in data.split('\n'):
        strings += 1
    return strings

def min_letter_count():
    letters_dict = {}
    for letter in data:
        if letter.lower() in alfabet:
            if letter.lower() in letters_dict:
                letters_dict[letter.lower()] += 1
            else:
                letters_dict[letter.lower()] = 1
    return min(letters_dict, key=letters_dict.get)


zen_file = open('zen.txt', 'r')
data = zen_file.read()
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = 0
words = 0
strings = 0


print(f'Количество букв в тексте: {letters_count(letters)}')
print(f'Количество слов в тексте: {words_count(words)}')
print(f'Количество строк в тексте: {strings_count(strings)}')
print(f'Наиболее редкая буква: {min_letter_count()}')
zen_file.close()
