
f = open("input.txt", "r")
moves = []
for line in f.readlines():
    moves.append(line.split())

#    x,y
h = [0,0]
t = [0,0] # The short tail
tail = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]  # The long tail

tail_pos = set()
tail_9_pos = set()

def check_for_tail(h, t):
    if h[0] == t[0] and (h[1]-t[1])**2 not in [0,1]:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
    elif h[1] == t[1] and (h[0]-t[0])**2 not in [0,1]:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
    elif abs(abs(h[0]) - abs(t[0])) == 1 and abs(abs(h[1]) - abs(t[1])) == 1:
        pass
    elif h[0] != t[0] and h[1] != t[1]:
        if h[0] - t[0] > 0:
            t[0] += 1
        else:
            t[0] -= 1

        if h[1] - t[1] > 0:
            t[1] += 1
        else:
            t[1] -= 1


def move_loop(moves, i, dir):
    for _ in range(moves):
        h[i] += dir
        check_for_tail(h, t)
        tail_pos.add((t[0], t[1]))

        for index in range(len(tail)):
            if index == 0:
                check_for_tail(h, tail[index])
            else:
                check_for_tail(tail[index - 1], tail[index])

            if index == len(tail)-1:
                tail_9_pos.add((tail[index][0], tail[index][1]))


def move_head(direction, moves):
    if direction == "R":
        move_loop(moves, 1, 1)
    if direction == "L":
        move_loop(moves, 1, -1)
    if direction == "U":
        move_loop(moves, 0, -1)
    if direction == "D":
        move_loop(moves, 0, 1)


for move in moves:
    move_head(move[0], int(move[1]))


print(f"Total tail positions: {len(tail_pos)}")
print(f"Total 9-tail positions: {len(tail_9_pos)}")
