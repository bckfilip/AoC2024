
def read_input(filename):
    matrix = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            matrix.append(list(line))

    return matrix


def beams():
    matrix = read_input("input.txt")
    visited = set()
    
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == "S":
                starti, startj = i, j
                trace(matrix, i + 1, j, visited)
    
    return matrix, starti, startj


def trace(matrix, row, col, visited):
    #check oobs
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return
    
    if (row, col) in visited:
        return
    
    visited.add((row, col))
    current = matrix[row][col]
    
    if current == ".":
        matrix[row][col] = "l"
        trace(matrix, row+1, col, visited)
        
    elif current == "l":
        trace(matrix, row+1, col, visited)
    
    elif current == "^":
        trace(matrix, row+1, col-1, visited)
        trace(matrix, row+1, col+1, visited)


def dfs(matrix, row, col, memo):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if row == rows:
        return 1  
    if col < 0 or col == cols:
        return 0
    
    if (row, col) in memo:
        return memo[(row, col)]

    paths = 0
    current = matrix[row][col]

    if current == "S" or current == "l":
        paths += dfs(matrix, row + 1, col, memo)
    elif current == "^":
        paths += dfs(matrix, row + 1, col - 1, memo)
        paths += dfs(matrix, row + 1, col + 1, memo)

    memo[(row, col)] = paths
    return paths

def timelines():
    matrix, starti, startj = beams()
    memo = {}
    paths_count = dfs(matrix, starti, startj, memo)
    
    return paths_count

if __name__ == "__main__":
    print(timelines())
