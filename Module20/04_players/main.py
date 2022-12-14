players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
temp_tuple = ()
result_list = [player + players[player] for player in players.keys()]
print(result_list)