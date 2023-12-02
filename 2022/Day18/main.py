import time

start_time = time.time()
f = open('input.txt', "r")

positions = []
for row in f.readlines():
    positions.append(tuple(int(x) for x in row.split(',')))


def separated_cube_sides(cubes):
    total_sum = 0
    for p in cubes:
        x, y, z = p
        cube_sides = 6
        for el in cubes:
            dx, dy, dz = el
            if abs(x - dx) + abs(y - dy) + abs(z - dz) == 1:
                cube_sides -= 1
        total_sum += cube_sides
    return total_sum


def neighbors(x, y, z):
    return ((x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),)


def in_grid(x, y, z):
    return -1 <= x and x <= 30 and -1 <= y and y <= 30 and -1 <= z and z <= 30


reached = {(0, 0, 0)}
stack = [[0, 0, 0]]
total_side_counter = 0
while len(stack) > 0:
    nb = neighbors(*stack.pop())

    total_side_counter += sum((1 for x in nb if x in positions))
    for n in nb:

        if in_grid(*n) and n not in reached and n not in positions:
            reached.add(n)
            stack.append(n)

exterior_side_counter = separated_cube_sides(positions)

print(f"Part 1: {exterior_side_counter}")
print(f"Part 2: {total_side_counter}")
print(time.time() - start_time)
