import os.path

first_tour = open(os.path.abspath('first_tour.txt'), 'r').read().splitlines()
secnd_tour = open(os.path.abspath('second_tour.txt'), 'w')

winners_list = []
for i in first_tour[1:]:
    if (i.split(' ')[2]) > first_tour[0]:
        winners_list.append(i)

lines_count = 1
secnd_tour.write(str(len(winners_list)) + '\n')
for result in sorted(winners_list):
    secnd_tour.write(f'{lines_count}) {result.split(" ")[0][0]}.{result.split(" ")[1]} {result.split(" ")[2]}\n')
    lines_count +=1
