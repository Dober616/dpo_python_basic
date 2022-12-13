players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
temp_tuple = ()
result_list = []
for player in players.keys():
    temp_tuple = player + players[player]
    result_list.append(temp_tuple)
result_list = tuple(result_list)

print(result_list)