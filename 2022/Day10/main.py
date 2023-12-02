f = open("input.txt", "r")

count_of_cycles = 0
crt_cycle = 0
x=1
signal = [20,60,100,140,180,220]
signal_strength = []
sprite_position = [1,2,3]
crt_row = ""
for line in f.readlines():
    if line.startswith("noop"):
        cycle = 1
    else:
        cycle = 2
        value = int(line.split()[1])

    for i in range(cycle):
        count_of_cycles += 1
        crt_cycle += 1
        if crt_cycle in sprite_position:
            crt_row += "#"
        else:
            crt_row += " "
        if len(crt_row) == 40:
            crt_cycle = 0
            print(crt_row)
            crt_row = ""

        if count_of_cycles in signal:
            signal_strength.append(x * count_of_cycles)

    if cycle == 2:
        x += value
        for i in range(3):
            sprite_position[i] += value

print(f"Total signal strength: {sum(signal_strength)}")
