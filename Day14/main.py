import time

start_time = time.time()
f = open("input.txt", "r")
input = [l for l in f.readlines() if l != "\n"]

cols = 700
rows = 700

map = [[0] * cols for _ in range(rows)]

bottom = 0
for line in input:
    indexes = [[int(x) for x in l.split(',')] for l in line.split(' -> ')]
    while True:
        x, y = indexes.pop(0)
        dx, dy = indexes[0]
        x, dx = max(x, dx), min(x, dx)
        y, dy = max(y, dy), min(y, dy)

        if x == dx:
            for y in range(dy, y + 1):
                map[y][x] = 1
        else:
            for x in range(dx, x + 1):
                map[y][x] = 1

        if len(indexes) == 1:
            break

        bottom = max(bottom, y + 2)


def drop_peace(x, y):
    if map[y][x] > 0:
        return None

    while y < rows - 1:
        if map[y + 1][x] == 0:
            y += 1
        elif map[y + 1][x - 1] == 0:
            y += 1
            x -= 1
        elif map[y + 1][x + 1] == 0:
            y += 1
            x += 1
        else:
            return (x, y)
    return None


def count_peaces():
    drops = 0
    while True:
        res = drop_peace(500, 0)
        if res is None:
            return drops
        map[res[1]][res[0]] = 2
        drops += 1


drops = count_peaces()
print(f"Part 1: {drops}")

map[bottom] = [2] * cols
drops += count_peaces()
print(f"Part 2: {drops}")
print("--- %s seconds ---" % (time.time() - start_time))
