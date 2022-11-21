def shift_symbols(my_word, shift):
    while shift > len(my_word):
        shift -= len(my_word)
    temp = my_word[-shift:] + my_word[:-shift]
    return temp


def caesar(letter_shift, my_word):
    encrypted_word = [alfabet[alfabet.index(letter) - len(alfabet) + letter_shift] if letter in alfabet else letter for
                      letter in my_word]
    return encrypted_word


alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = 3
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
encrypted_text = []
for each_word in text:
    encrypted_text.append(''.join(caesar(51, shift_symbols(each_word, shift))))
    each_word.replace('/', '\n')
    if '/' in each_word:
        shift += 1
new_text = (' '.join(encrypted_text).replace('/', '\n'))
print(new_text.replace('(', "'").replace('+', '*').replace('-', ',').replace('.', '-').replace('"', '!'))