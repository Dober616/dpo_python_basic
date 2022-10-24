def count_letters():
    count = 0
    for sym in word:
        if sym == letter:
            count += 1
    return(count)
word = input('Введите слово: ')
word_letters = []
for letter in word:
    if count_letters() == 1:
        word_letters.append(letter)
print('Количество уникальных букв: ', len(word_letters))
