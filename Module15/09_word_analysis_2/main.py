word = input('Введите слово: ')
lenght = len(word)
x = 0
y = lenght-1
count = 0
while x <= y:
    if word[x] != word[y]:
        print('Слово не является полиндромом')
        break
    else:
        x += 1
        y -= 1
        count += 1
    if count == lenght // 2:
        print('Слово является полиндромом')
