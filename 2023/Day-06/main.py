import time as timetime
import numpy

start = timetime.time()

f = open('input.txt', 'r')
input = f.readlines()

time = [int(x) for x in input[0].split(":")[1].split()]
dist = [int(x) for x in input[1].split(":")[1].split()]

time_2 = [int("".join(list(map(str, time))))]
dist_2 = [int("".join(list(map(str, dist))))]

c_ways = 0
ways = []

for i in range(len(time)):
    c_time = time[i]
    c_dist = dist[i]
    c_ways = 0
    for t in range(c_time):
        travel_distance = (c_time - t ) * t
        if travel_distance > c_dist:
            c_ways += 1
    ways.append(c_ways)
print(f"Answer part 1: {numpy.prod(ways)}")

c_ways = 0
step = 60000
center_to_left = int(time_2[0] /2)
center_to_right = int((time_2[0]/ 2) + 1)
c_time = time_2[0]
c_dist = dist_2[0]
def to_left():
    c_ways = 0
    for cursor in range(center_to_left-step, 0, -step):
        travel_distance = (c_time - cursor) * cursor
        if travel_distance > c_dist:
            c_ways += step
        else:
            for c in range(cursor + step, 0, -1):
                travel_distance = (c_time - c) * c
                if travel_distance > c_dist:
                    c_ways += 1
            break
    return c_ways

def to_right():
    c_ways = 0
    for cursor in range(center_to_right + step, time_2[0], step):
        travel_distance = (c_time - cursor) * cursor
        if travel_distance > c_dist:
            c_ways += step
        else:
            for c in range(cursor - step, time_2[0]):
                travel_distance = (c_time - c) * c
                if travel_distance > c_dist:
                    c_ways += 1
            break

    return c_ways

c_ways += to_left()
c_ways += to_right()

print("Answer for part 2: ", c_ways)
print(timetime.time() - start)