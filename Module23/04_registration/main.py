import re


def mail_check(mail):
    sample = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if re.match(sample, mail):
        return True
    return None


list_string = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
with open('registrations.txt', 'r', encoding='utf8') as protocol:
    with open('registratioons_bed.txt', 'w') as bad_santa:
        for line in protocol:
            line_string = line.split(' ')
            list_string += 1
            if not line_string[0].isalpha():
                bad_santa.write(f'Запись № {list_string}. Ошибка в  имени. {line}')
                sum_1 += 1
            elif not mail_check(line_string[1]):
                bad_santa.write(f'Запись № {list_string}. Ошибка в эл. адресе. {line}')
                sum_2 += 1
            try:
                if 1 > int(line_string[2]) > 99:
                    bad_santa.write(f'Запись № {list_string}. Ошибка в возрасте. {line}')
                    sum_3 += 1
            except IndexError:
                bad_santa.write(f'Запись № {list_string}. Заполнены не все поля. {line}')
                sum_3 += 1
            except ValueError:
                bad_santa.write(f'Запись № {list_string} . Ошибка в возрасте. {line}')
                sum_3 += 1
print(f'Ошибки в именах: {sum_1}')
print(f'Ошибки в адресе: {sum_2}')
print(f'Ошибки в возрасте:  {sum_3}')
