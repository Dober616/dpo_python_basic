def shift_symbols(my_word, shift):
    temp = my_word[shift:len(word)] + my_word[0:shift]
    return temp
def caesar(letter_shift, my_word):
    encrypted_word = [alfabet[alfabet.index(letter) - len(alfabet) + letter_shift]
                         if letter in alfabet else letter for letter in my_word]
    return encrypted_word
word = 'jdjufyqm'  # shift_symbols(word,1)
alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(word)
print(''.join(caesar(51, shift_symbols(word, abs(len(word) + 3)))))
text = 'fTjnqm tj scfuuf ibou fy/dpnqm'.split()
encrypted_text = []
for each_word in text:
    encrypted_text.append(''.join(caesar(51, shift_symbols(each_word, abs(len(each_word) - 5)))))
print(encrypted_text)

for i in range(0,len(encrypted_text) + 1, 20):
    print(encrypted_text[i])

# 3 'Beutiful', 'is', 'better', 'than', 'ugly/'
# 4 ‘Explicit', 'is', 'better', 'than', 'impicit/‘
# 5 'Simple', 'si', 'better', 'anth', 'complex/'