import time
start_time = time.time()

f = open("input.txt", "r")
input = f.readlines()

sum_ids = 0
id = 0
sum_part2 = 0

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

current_max_colors = {
    "red": 0,
    "green": 0,
    "blue": 0,
}
#  Part 1
for line in input:
    id += 1
    add = True

    [_, game] = line.split(": ")
    for hand in game.strip().split('; '):
        hand = hand.split(', ')
        for color in hand:
            quantity, col = color.split(' ')
            if max_cubes[col] < int(quantity):
                add = False
                break
        if not add:
            break
    if add:
        sum_ids += id


#  Part 2
for line in input:

    [_, game] = line.split(": ")
    for hand in game.strip().split('; '):
        hand = hand.split(', ')
        for color in hand:
            quantity, col = color.split(' ')
            if current_max_colors[col] < int(quantity):
                current_max_colors[col] = int(quantity)

    game_points = current_max_colors["red"] * current_max_colors['green'] * current_max_colors['blue']

    sum_part2 += game_points
    current_max_colors = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

print(sum_part2)
print(time.time() - start_time)