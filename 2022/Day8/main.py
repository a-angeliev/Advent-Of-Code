
input_list = []
f = open("input.txt", "r")
matrix = f.readlines()
for r in range(0, len(matrix)):
    input_list.append([])
    input_list[r] = [int(matrix[r][c]) for c in range(0, len(matrix[r]) - 1)]


matrix = input_list
matrix_t = list(zip(*input_list))

num_rows = len(matrix)
num_cols = len(matrix[0])

trees = []

for c in range(1, num_cols - 1):
    vis_num = matrix[0][c]
    for r in range(1, num_rows-1):
        if matrix[r][c] > vis_num:
            trees.append([r,c])
            vis_num = matrix[r][c]

for c in range(1, num_cols - 1):
    vis_num = matrix[num_rows - 1][c]
    for r in range(num_rows-1, 0, -1):
        if matrix[r][c] > vis_num:
            trees.append([r,c])
            vis_num = matrix[r][c]

for r in range(1, num_rows-1):
    vis_num=matrix[r][0]
    for c in range(1, num_cols - 1):
        if matrix[r][c] > vis_num:
            trees.append([r,c])
            vis_num = matrix[r][c]

for r in range(1, num_rows-1):
    vis_num = matrix[r][num_cols - 1]
    for c in range(num_cols - 1, 0, -1):
        if matrix[r][c] > vis_num:
            trees.append([r,c])
            vis_num = matrix[r][c]


unique_list = []
for x in trees:
    if x not in unique_list:
        unique_list.append(x)
visible_trees = ((num_cols - 2) * 2 + (num_rows - 2) * 2 + 4) + len(unique_list)
print("visible trees:", visible_trees)

# PART 2 //////////////////////////////////////////////////

best_score = 0

for r in range(1, num_rows-1):

    for c in range(1, num_cols - 1):
        current_tree_high = matrix[r][c]
        l = 0
        ri = 0
        u = 0
        d = 0

        for left in range(c-1, -1, -1):
            if matrix[r][left] >= current_tree_high:
                l += 1
                break
            l += 1

        for right in range(c+1, num_cols):
            if matrix[r][right] >= current_tree_high:
                ri += 1
                break
            ri += 1

        for up in range(r-1, -1,-1):
            if matrix_t[c][up] >= current_tree_high:
                u += 1
                break
            u += 1

        for down in range(r+1, num_rows):
            if matrix_t[c][down] >= current_tree_high:
                d += 1
                break
            d += 1

        current_result = l * ri * u * d

        if current_result > best_score:
            best_score = current_result

print("best score:", best_score)


