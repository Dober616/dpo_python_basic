def playlist():
    for i in violator_songs:
        if i[0] == song:
            return i[1]
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
my_playlist = []
duration = 0
songs_count = int(input('Сколько песен выбрать?: '))
for i in range (songs_count):
    print('Название', i+1, 'песни: ', end='')
    song = input()
    duration += playlist()
print('Общее время звучания песен: ', duration, 'минут')