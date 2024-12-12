
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(map(int, row)) for row in rows]  

    return matrix

def dfs(x, y, matrix, visited, current_number, path, all_paths):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


    path.append((x, y))

    if matrix[x][y] == 9:
        all_paths.append(list(path)) 
    else:
        visited[x][y] = True

        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if (
                0 <= new_x < len(matrix)
                and 0 <= new_y < len(matrix[0])
                and not visited[new_x][new_y]
                and matrix[new_x][new_y] == current_number + 1
            ):
                dfs(new_x, new_y, matrix, visited, current_number + 1, path, all_paths)

        visited[x][y] = False 

    path.pop()  


def find_paths():
    matrix = read_input()
    all_paths = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                dfs(i, j, matrix, visited, 0, [], all_paths)

    return all_paths

all_paths = find_paths()
print(f"Total unique paths found: {len(all_paths)}")
# for path in all_paths:
#     print(path)
