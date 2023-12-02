import time
start = time.time()
f = open('input.txt', "r")

number = {}
operations = {}

for line in f.readlines():
    name, right_site = line.split(": ")
    right_site = right_site.removesuffix("\n").split(" ")
    if len(right_site) == 1:
        number[name] = int(right_site[0])
    else:
        operations[name] = [right_site[0], right_site[1], right_site[2]]


def find_root():
    while True:
        for name, value in operations.items():
            if value[0] in number and value[2] in number:
                result = eval(f"{number[value[0]]}" + f"{value[1]}" + f"{number[value[2]]}")
                del operations[name]
                number[name] = int(result)
                if name == "root": return result
                break


print(f"Part 1: {find_root()}")
print(time.time() - start)