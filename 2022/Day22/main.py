f = open("input.txt")
raw_input = f.readlines()
raw_path = raw_input[-1]
board = []

for i in range(len(raw_input) - 2):
    board.append([el for el in raw_input[i].removesuffix("\n")])

path = []
el = ''
while raw_path:
    sym = raw_path[0]
    raw_path = raw_path[1:]
    if sym == "L" or sym == "R":
        path.append(int(el))
        path.append(sym)
        el = ""
    else:
        el += sym

if el != "":
    path.append(int(el))
max_row_len = max([len(x) for x in board])
for el in board:
    if len(el) != max_row_len:
        while len(el) != max_row_len:
            el.append(" ")

ROW_INDEX = 0
COL_INDEX = min([board[0].index(el) for el in board[0] if el == "."])
DIRECTION = 0

ROW_LEN = len(board)
COL_LEN = len(board[0])


def change_direction(command):
    if command == "L":
        return DIRECTION - 1 if DIRECTION - 1 != -1 else 3
    else:
        return DIRECTION + 1 if DIRECTION + 1 != 4 else 0


def find_opposite(row,col):
    if DIRECTION == 0:
        for i in range(COL_LEN):
            if board[row][i] == "." or board[row][i] == "#":
                return (row, i)
    elif DIRECTION == 1:
        for i in range(ROW_LEN):
            if board[i][col] == "." or board[i][col] == "#":
                return (i, col)
    elif DIRECTION == 2:
        for i in range(COL_LEN-1, -1, -1):
            if board[row][i] == "." or board[row][i] == "#":
                return (row, i)
    else:
        for i in range(ROW_LEN - 1, -1, -1):
            if board[i][col] == "." or board[i][col] == "#":
                return (i, col)


def next_position(row, col):
    next = {
        0: (row, col + 1),
        1: (row + 1, col),
        2: (row, col - 1),
        3: (row - 1, col)
    }

    next_row, next_col = next[DIRECTION]
    if 0 <= next_row < ROW_LEN and 0 <= next_col < COL_LEN:
        if board[next_row][next_col] != " ":
            return (next_row, next_col)

    return find_opposite(row,col)


def check_is_wall(next):
    return True if board[next[0]][next[1]] == "#" else False


def move(moves):
    row, col = ROW_INDEX, COL_INDEX
    for move in range(moves):
        next = next_position(row, col)
        is_wall = check_is_wall(next)
        if not is_wall:
            row, col = next
        else:
            break

    return row, col


for el in path:
    if el == "L" or el == "R":
        DIRECTION = change_direction(el)
    else:
        ROW_INDEX, COL_INDEX = move(el)

print(f"Part 1: {(ROW_INDEX+1)*1000 + (COL_INDEX+1)*4 + DIRECTION}")
