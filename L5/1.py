games = []

while True:
    game = input('название игры (для выхода введите 0): ')
    if game == '0':
        break
    if game not in games:
        games.append(game)

games.sort()
print(games)