input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green


s = 0
for l in lines:
    limits = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    game, records = l.split(": ")
    game = game.replace("Game ", "")
    game = int(game)

    records = records.split("; ")
    
    possible = True
    for rec in records:
        cubes = rec.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            limits[color] = max(limits[color], int(count))
    
    p = 1
    for k in limits:
        p *= limits[k]
    s += p
print(s)