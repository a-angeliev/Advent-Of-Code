import time

start_time = time.time()
rocks = {
    1: [[0, 2], [0, 3], [0, 4], [0, 5]],
    2: [[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]],
    3: [[2, 4], [1, 4], [0, 2], [0, 3], [0, 4]],
    4: [[0, 2], [1, 2], [2, 2], [3, 2]],
    5: [[0, 2], [0, 3], [1, 2], [1, 3]]
}
next_rock = 1
gas_pattern = open("input.txt", 'r').read()
# gas_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
cave = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]

highest = 0
height = [1]


def drop_rock(highest_i):
    highest_index = highest_i
    rock = rocks[next_rock]
    if next_rock != 5:
        new_next_rock = next_rock + 1
    else:
        new_next_rock = 1

    new_rock_indexes = [[el[0] + 4 + highest_index, el[1]] for el in rock]
    return new_rock_indexes, new_next_rock


def check_if_possible_to_move_left_or_right(rock_indexes, direction):
    for index in rock_indexes:
        if [index[0], index[1] + direction] not in cave and 0 <= index[1] + direction <= 6:
            pass
        else:
            return False
    return True


def move_left_or_right(rock_indexes, direction):
    new_rock_indexes = []
    for index in rock_indexes:
        new_rock_indexes.append([index[0], index[1] + direction])
    return new_rock_indexes


def move_down(rock_indexes):
    for index in rock_indexes:
        if [index[0] - 1, index[1]] in cave:
            current_row_highest_index = 0
            for el in rock_indexes:
                current_row_highest_index = max(current_row_highest_index, el[0])
                cave.append(el)
            height.append(current_row_highest_index - sum(height))
            return True, current_row_highest_index
    new_rock_indexes = [[index[0] - 1, index[1]] for index in rock_indexes]
    return new_rock_indexes, None


def dropping(starting_rock_indexes):
    pattern = gas_pattern
    current_rock_indexes = starting_rock_indexes

    direction, pattern = pattern[0:1], pattern[1:]

    while True:
        if direction == ">":
            if check_if_possible_to_move_left_or_right(current_rock_indexes, 1):
                current_rock_indexes = move_left_or_right(current_rock_indexes, 1)
        else:
            if check_if_possible_to_move_left_or_right(current_rock_indexes, -1):
                current_rock_indexes = move_left_or_right(current_rock_indexes, -1)

        current_rock_indexes, row_highest = move_down(current_rock_indexes)
        pattern += direction
        if current_rock_indexes == True:
            return pattern, row_highest
        direction, pattern = pattern[0:1], pattern[1:]


for _ in range(10000):
    if len(cave) > 200:
        cave = cave[50:]
    rock_indexes, next_rock = drop_rock(highest)
    gas_pattern, row_highest = dropping(rock_indexes)
    highest = max(highest, row_highest)

MAX_SKIP = 200
MAX_PATTERN = 2000


def find_pattern():
    for skip_first in range(MAX_SKIP):
        r = height[skip_first:]
        for i in range(20, MAX_PATTERN, 10):
            if r[0:i] == r[i:2 * i]:
                return skip_first, i


def height_by_rocks(rocks_number):
    skip, pattern = find_pattern()
    skip_h = sum(height[:skip])
    pattern_h = sum(height[skip:skip + pattern])

    times = (rocks_number + 1 - skip) // pattern
    leftover = (rocks_number + 1 - skip) % pattern
    leftover_h = sum(height[skip:skip + leftover])

    return skip_h + pattern_h * times + leftover_h


print(f"Part 1: {sum(height[:2023])}")
print(f"Part 2: {height_by_rocks(1000000000000)}")
print(start_time - time.time())
