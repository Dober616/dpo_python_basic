import os.path

first_tour = open(os.path.abspath('first_tour.txt'), 'r').read().splitlines()
secnd_tour = open(os.path.abspath('second_tour.txt'), 'w')
scores = int(first_tour[0])
count = 1
for line in first_tour[1:]:
    if int(line.split(' ')[2]) > scores:
        secnd_tour.write(f'{count}) {line.split(" ")[0][0]}. {line.split(" ")[1]} {line.split(" ")[2]}\n')
        count += 1
