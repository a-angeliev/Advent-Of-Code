import re
import time
start = time.time()
file1 = open('input.txt', 'r')
lines = file1.readlines()

numbers = [int(x) for x in re.findall(r'(\b\d+\b)', lines[0])]
print(numbers)
seeds = []

nc = 0
while(nc < len(numbers)):
    seeds.append({ 'x0': numbers[nc], 'n0': numbers[nc + 1]})
    nc += 2

# helpers
planted_seeds = []
cursor = 1

# parse the document section by section
while(cursor < len(lines)):
    # skip empty and info row
    cursor+=2

    # get the current section
    current_map = []
    while(cursor < len(lines) and lines[cursor] != '\n'):
        line = [int(x) for x in re.findall(r'(\b\d+\b)', lines[cursor])]
        current_map.append({ 'y1': line[0], 'x1': line[1], 'n1': line[2]})
        cursor += 1

  # plant the seeds
    while len(seeds) > 0:
         # take one seed off the stack of seeds
        seed = seeds.pop(0)
        planted = False

        # try to plant it in the section
        for m in current_map:
            # case 1: x0 - x1 - x0+n0 - x1+n1
            if seed['x0'] <  m['x1'] and ((seed['x0'] + seed['n0']) > m['x1']) and (seed['x0'] + seed['n0']) <= (m['x1'] + m['n1']):
                planted_seeds.append({ 'x0': m['y1'], 'n0': seed['x0'] + seed['n0'] - m['x1']})
                seeds.append({'x0': seed['x0'], 'n0': m['x1'] - seed['x0'] })
                planted = True
                break

            # case 2: x1 - x0 - x0+n0 - x1+n1
            elif seed['x0'] >=  m['x1'] and (seed['x0'] + seed['n0']) <= (m['x1'] + m['n1']):
                planted_seeds.append({ 'x0': m['y1'] + seed['x0'] - m['x1'], 'n0': seed['n0']})
                planted = True
                break

            # case 3: x1 - x0 - x1+n1 - x0+n0
            elif seed['x0'] >=  m['x1'] and seed['x0'] <  m['x1'] + m['n1'] and (seed['x0'] + seed['n0']) > (m['x1'] + m['n1']):
                planted_seeds.append({ 'x0': m['y1'] + seed['x0'] - m['x1'], 'n0': m['x1'] + m['n1'] - seed['x0']})
                seeds.append({'x0': m['x1'] + m['n1'], 'n0': seed['x0'] + seed['n0'] - (m['x1'] + m['n1']) })
                planted = True
                break

        # if seed could not be planted at all
        if not planted:
            planted_seeds.append(seed)

    seeds = planted_seeds
    planted_seeds = []

seeds.sort(key=lambda x: x['x0'])
print(time.time()- start)
print(seeds[0]['x0'])