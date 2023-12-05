import time
start = time.time()

f = open("input.txt",'r')
input = f.readlines()

seeds_input = input[0].split(": ")[1].strip().split(" ")

maps = []
next_number = -1
min_seed_number = -1
end_location = 9999999999999999999999999
min_end_location = 9999999999999999999999999
STEP = 30000
seeds = []

for row in range(len(input)):
    if input[row].startswith(("seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location")):
        name = input[row].split(" ")[0]
        maps.append({name: []})
        continue

    if input[row] == "\n" or row == 0:
        continue

    for ind in range(len(maps)):
        key_list = [key for key, val in maps[ind].items() if key == name]
        if len(key_list) == 1:
            maps[ind][name].append(input[row].strip().split(' '))


for i in range(0, len(seeds_input), 2):
    seeds = [int(seed) for seed in range(int(seeds_input[i]), (int(seeds_input[i]) + int(seeds_input[i + 1])), STEP)] + seeds


def calculate_end_location(seed, end_location):
    next_number = seed
    for map in maps:
        for key, value in map.items():
            for row in value:
                dest, source, rng = [int(i) for i in row]
                if source <= next_number < (source + rng):
                    next_number = next_number - source + dest
                    break

    return min([next_number, end_location])


#  Part 1
for seed in seeds_input:
    end_location = calculate_end_location(int(seed), end_location)

print("End location for part 1:", end_location)

#  Part 2
for loop in range(2):
    if loop == 1:
        seeds = [int(seed) for seed in range(min_seed_number - STEP, (min_seed_number + STEP))]

    for seed in seeds:
        end_location = calculate_end_location(seed, end_location)

        if end_location < min_end_location:
            min_seed_number = seed
            min_end_location = end_location

print("End location for part 2:", end_location)

print(time.time() - start)