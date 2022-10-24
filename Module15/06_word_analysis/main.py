

word = input('Введите слово: ')
count = 0
for letter in word:
    for symbol in word:
        if letter == symbol:
            count +=1
print(count)