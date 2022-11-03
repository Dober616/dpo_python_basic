skates_sizes = []
legs_sizes = []
max_people = 0
skates_count = int(input('Количество коньков: '))
for i in range(skates_count):
    print('Размер', i + 1, '-й пары: ', end='')
    skate_size = int(input())
    skates_sizes.append(skate_size)
people_count = int(input('Количество людей: '))
for i in range(people_count):
    print('Размер ноги', i + 1, '-го человека: ', end='')
    leg_size = int(input())
    legs_sizes.append(leg_size)
skates_sizes.sort()
legs_sizes.sort(reverse=True)
for leg in legs_sizes:
    for skate in skates_sizes:
        if leg > skate:
            pass
        else:
            max_people += 1
            break
print('Наибольшее количество людей, которые могут взять ролики: ', max_people)
