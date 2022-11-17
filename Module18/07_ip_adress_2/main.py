def separation_parts():
    if len(ip_adress.split('.')) != 4:
        return False
    else:
        return True


def full_numm():
    for i in ip_adress.split('.'):
        if i.isdigit():
            pass
        else:
            return i


def ip_range():
    for part in ip_adress.split('.'):
        if int(part) < 256:
            pass
        else:
            return part
    return True


ip_adress = input('Введите IP: ')

if separation_parts() == False:
    print('Адрес - это 4 числа, разделенные точками')
else:
    if full_numm():
        print(full_numm(), '- это не целое число')
    else:
        if ip_range() == True:
            print('Нормальный IP-адрес: ', ip_adress)
        else:
            print(ip_range(), 'превышает 255')
