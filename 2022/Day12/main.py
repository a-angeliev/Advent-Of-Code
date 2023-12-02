f = open("input.txt", "r")
matrix = []
for line in f.readlines():
    matrix.append([x for x in line.removesuffix('\n')])

for i in range(len(matrix)):
    if "S" in matrix[i]:
        S = [i, matrix[i].index("S")]

que = [S]

R = len(matrix)
L = len(matrix[0])

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

a = 2

is_checked = [[False for _ in range(L)] for _ in range(R)]
visualise = [[0 for _ in range(L)] for _ in range(R)]


def check_high(current_node, neighbour):
    if neighbour == "E":

        if ord("z") - ord(current_node) < 2:
            return True
    else:
        if current_node == "S":
            current_node = "a"
        if ord(neighbour) - ord(current_node) < 2:
            return True
    return False


def node_neighbours(x, y):
    for i in range(4):
        dx = x + dRow[i]
        dy = y + dCol[i]

        if 0 <= dx < R and 0 <= dy < L:
            if check_high(matrix[x][y], matrix[dx][dy]) and is_checked[dx][dy] == False:
                is_checked[dx][dy] = True
                yield [dx,dy]


steps = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

while len(que) > 0:
    flag = False
    x, y = que.pop(0)

    for el in node_neighbours(x,y):
        que.append(el)
        nodes_in_next_layer += 1
        if matrix[el[0]][el[1]] == "E":
            flag = True

    nodes_left_in_layer -= 1
    if nodes_left_in_layer == 0:
        nodes_left_in_layer = nodes_in_next_layer
        nodes_in_next_layer = 0
        steps += 1

    if flag:
        if nodes_in_next_layer != 0:
            steps += 1
        break
print(steps)