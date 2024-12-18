def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()
    parts = input_string.strip().split("\n\n")

    grid_str = parts[0]
    list_str = parts[1]

    #matrix
    grid = [list(row) for row in grid_str.split("\n")]

    # moves
    moves = list_str.replace("\n", "")

    return grid, moves


def find_startpos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                return i,j
    return 0


def check_next(pos, matrix, direction):

    direction_map = {
        "^": (-1, 0),  # up
        ">": (0, 1),   # right
        "v": (1, 0),   # down
        "<": (0, -1)   # left
    }
    
    # curr dir
    di, dj = direction_map[direction]

    next_i, next_j = pos[0] + di, pos[1] + dj
    
    if matrix[next_i][next_j] == ".":
        matrix[pos[0]][pos[1]] = "."
        matrix[next_i][next_j] = "@"
        return (next_i, next_j)
    
    #wall or obstacle
    elif matrix[next_i][next_j] == "#":
        return pos
    
    elif matrix[next_i][next_j] == "O":

        new_pos = check_next((next_i, next_j), matrix, direction)

        if new_pos != (next_i, next_j):

            # move the "O" if can, update its position
            matrix[next_i][next_j] = "."
            matrix[new_pos[0]][new_pos[1]] = "O"

            # Move @ to the new position
            matrix[pos[0]][pos[1]] = "."
            matrix[next_i][next_j] = "@"
            return (next_i, next_j)
        
    return pos


def main():
    matrix, moves = read_input()
    pos = find_startpos(matrix)

    for move in moves:
       pos = check_next(pos, matrix, move)
    gps = 0
    sum_gps = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                sum_gps += ((i * 100) + j)

    return sum_gps

sum_gps = main()
print(sum_gps)