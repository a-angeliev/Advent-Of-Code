import time

start_time = time.time()
f = open("input.txt", "r")
lines = [line.removesuffix('\n') for line in f.readlines()]


def distance(x, y, dx, dy):
    return abs(x - dx) + abs(y - dy)


def row_signals(r):
    row_coverage = set()
    for sensor in sensors:
        y, x, d = sensor
        if abs(y - r) <= d:
            row_range = d - abs(y - r)
            row_coverage.add((x - row_range, x + row_range))
    return row_coverage


def overlap(r):
    result = list(sorted(row_signals(r)))
    a = max(result[0])
    b = min(result[0])

    for i in range(len(result)):

        x, y = result[i][0], result[i][1]
        if b <= x <= a or b <= y <= a:
            a = max(a, x, y)
            b = min(b, x, y)
        else:
            print(f"Part 2: {(a + 1) * 4000000 + r}")
            return None

    return [b, a]


row = 2000000
part_2_rows = 4000000

sensors = []
for line in lines:
    line = line.removeprefix("Sensor at x=").replace("y=", "").replace(": closest beacon is at x=", ', ')
    x, y, dx, dy = [int(x) for x in line.split(", ")]
    sensors.append([y, x, distance(y, x, dy, dx)])

l, r = overlap(row)
print(f"Part 1: {abs(l - r)}")

for r in range(part_2_rows):
    res = overlap(r)
    if res is None:
        break

print("--- %s seconds ---" % (time.time() - start_time))
