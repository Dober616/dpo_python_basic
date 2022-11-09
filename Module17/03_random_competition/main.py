import random
first_team = [round(random.uniform(5, 10), 2) for _ in range(10)]
secnd_team = [round(random.uniform(5, 10), 2) for _ in range(10)]

print('Первая команда: ', first_team)
print('Вторая команда: ', secnd_team)
winners = [(first_team[x] if first_team[x] > secnd_team[x] else secnd_team[x]) for x in range(10)]
print('Победители тура: ', winners)
