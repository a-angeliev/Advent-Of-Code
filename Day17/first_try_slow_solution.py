# DOESN'T WORK APPROPRIATELY. TOO SLOW
rocks = {
    1: [[[0, 0, 1, 1, 1, 1, 0]], 2, 1],
    2: [[[0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]], 1, 3],
    3: [[[0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 1, 0, 0]], 2, 2],
    4: [[[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0]], 2, 4],
    5: [[[0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0]], 2, 3]
}

cave = [[2, 2, 2, 2, 2, 2, 2]]
next_rock = 1
f = open('input.txt', "r")
gas_pattern = f.read()
# gas_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def clear_empty_space():
    for el in cave[::-1]:
        if 2 not in el:
            cave.remove(el)
        else:
            break


def drop_next_rock():
    for i in range(3):
        cave.append([0, 0, 0, 0, 0, 0, 0])
    for el in rocks[next_rock][0][::-1]:
        cave.append(el)
    if next_rock == 5:
        return 1
    else:
        return next_rock + 1


def move_left_or_right(direction):
    for row in cave[::-1]:
        row_index = cave.index(row)
        if 1 in row:
            new_row = row.copy()
            for index in range(7):
                if new_row[index] == 1:
                    new_row[index] = 0

            for i in range(7):
                if row[i] == 1:
                    new_row[i + direction] = 1
            cave[row_index] = new_row


def is_movable(direction):
    for row in cave[::-1]:
        if 1 in row:
            for i in range(7):
                if row[i] == 1:
                    if 0 <= i + direction <= 6:
                        if row[i + direction] != 2:
                            pass
                        else:
                            return
                    else:
                        return
    move_left_or_right(direction)


def end_rock():
    for row_index in range(len(cave)):
        if 1 in cave[row_index]:
            for el_index in range(len(cave[row_index])):
                if cave[row_index][el_index] == 1:
                    cave[row_index][el_index] = 2
    return True


def move_down():
    if len(cave) > 500:
        l = len(cave) - 500
    else:
        l = 0
    for row_index in range(l, len(cave)):
        if 1 in cave[row_index]:
            for el_index in range(7):
                if cave[row_index][el_index] == 1:
                    if cave[row_index - 1][el_index] != 2:
                        pass
                    else:
                        return end_rock()

    indexes = []
    for row_index in range(l, len(cave)):

        if 1 in cave[row_index]:
            for el_index in range(7):
                if cave[row_index][el_index] == 1:
                    cave[row_index][el_index] = 0
                    indexes.append([row_index - 1, el_index])

    for x, y in indexes:
        cave[x][y] = 1

    return False


def dropping():
    pattern = gas_pattern
    while True:

        direction, pattern = pattern[0:1], pattern[1:]
        if direction == ">":
            is_movable(1)
        else:
            is_movable(-1)

        end = move_down()
        pattern += direction
        if end:
            return pattern


for _ in range(2022):
    clear_empty_space()
    next_rock = drop_next_rock()
    gas_pattern = dropping()

for row in cave[::-1]:
    print(row)
clear_empty_space()
print(len(cave) - 1)
