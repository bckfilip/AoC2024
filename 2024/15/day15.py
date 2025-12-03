
def read_input():
    with open("exinput.txt", "r") as file:
        input_string = file.read()
    parts = input_string.strip().split("\n\n")
    grid_str, list_str = parts
    grid = [list(row) for row in grid_str.split("\n")]
    moves = list_str.replace("\n", "")
    return grid, moves

def find_startpos(matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == "@":
                return i, j
    return 0, 0

def resize_matrix(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for char in row:
            if char == "@":
                new_row.extend(["@", "."])
            elif char == "#":
                new_row.extend(["#", "#"])
            elif char == "O":
                new_row.extend(["[", "]"])
            elif char == ".":
                new_row.extend([".", "."])
        new_matrix.append(new_row)
    return new_matrix

def check_next(pos, matrix, direction):
    direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    di, dj = direction_map[direction]
    next_i, next_j = pos[0] + di, pos[1] + dj

    if 0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0]):
        if matrix[next_i][next_j] == ".":
            matrix[pos[0]][pos[1]], matrix[next_i][next_j] = ".", "@"
            return next_i, next_j
        elif matrix[next_i][next_j] == "[":
            box_positions = []
            current_i, current_j = next_i, next_j
            while 0 <= current_i < len(matrix) and 0 <= current_j < len(matrix[0]) and matrix[current_i][current_j] in ["[", "]"]:
                if matrix[current_i][current_j] == "[":
                    box_positions.append((current_i, current_j))
                    if 0 <= current_j + 1 < len(matrix[0]) and matrix[current_i][current_j + 1] == "]":
                        box_positions.append((current_i, current_j + 1))
                current_i += di
                current_j += dj

            if 0 <= current_i < len(matrix) and 0 <= current_j < len(matrix[0]) and matrix[current_i][current_j] == ".":
                for bi, bj in reversed(box_positions):
                    matrix[bi + di][bj + dj], matrix[bi][bj] = matrix[bi][bj], "."
                matrix[pos[0]][pos[1]], matrix[next_i][next_j] = ".", "@"
                return next_i, next_j
    return pos

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))
    print()

def main():
    grid, moves = read_input()
    matrix = resize_matrix(grid)
    pos = find_startpos(matrix)

    for move in moves:
        pos = check_next(pos, matrix, move)

    print("Final Matrix:")
    print_matrix(matrix)

    sum_gps = sum((i * 100 + j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char in ["[", "]"])
    return sum_gps

sum_gps = main()
print(f"Sum of GPS: {sum_gps}")
