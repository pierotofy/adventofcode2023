input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

s = 0
for l in lines:
    game, records = l.split(": ")
    game = game.replace("Game ", "")
    game = int(game)

    records = records.split("; ")
    
    possible = True
    for rec in records:
        cubes = rec.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            if int(count) > limits[color]:
                possible = False
                break
        if not possible:
            break
    
    if possible:
        s += game

print(s)