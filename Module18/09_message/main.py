def punctuation(word):
    for symbol in word:
        if symbol.isalpha():
            pass
        else:
            return symbol
    return True

message = 'Это задание очень! простое.'.split(' ')

encrypted_message = [x[::-1] if punctuation(x) == True else x[-2:0:-1] + x[-1] for x in message]
print(' '.join(encrypted_message))

