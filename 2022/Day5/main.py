
f = open("starting_crates.txt", "r")
crates = []
for line in f.readlines():
    crates.append([line[el] for el in range(1,len(line), 4)])
f.close()


f = open("input.txt", "r")
moves = []
for line in f.readlines():
    line_list = line.split(' ')
    moves.append([int(line_list[i].removesuffix("\n")) for i in range(1, len(line_list), 2)])


crates = [list(el) for el in list(zip(*crates[::-1]))]
for i in range(len(crates)):
    crates[i] = list(filter(lambda a: a != " ", crates[i]))


def crane(qty, p1, p2):
    for i in range(qty):
        crates[p2-1].append(crates[p1 - 1].pop())


for el in moves:
    crane(el[0], el[1], el[2])

string = ""
for el in crates:
    string += el.pop()
print(string)
