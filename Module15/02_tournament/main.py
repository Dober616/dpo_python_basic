team = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_team = []
for name in team:
    if (team.index(name) + 1) % 2 == 0:
        new_team.append(name)
print(new_team)