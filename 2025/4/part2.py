def read_input(filename):
    matrix = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            matrix.append(list(line))

    return matrix

def forklift(matrix):
    rolls = 0
    for i,row in enumerate(matrix):
        for j,element in enumerate(row):
            if element == "@":
                pos = (i,j)
                if check_surroundings(pos, matrix):
                    rolls += 1
                    matrix[i][j] = "."
    return matrix, rolls


def check_surroundings(pos, matrix):
    count = 0
    x, y = pos
    rows = len(matrix)
    cols = len(matrix[0])
    
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if matrix[nx][ny] == "@":
                count += 1

    return count < 4

def exhaust():
    matrix = read_input("input.txt")
    total_rolls = 0
    while True:
         matrix, rolls = forklift(matrix)
         total_rolls += rolls
         if rolls == 0:
            break
    
    return matrix, total_rolls

if __name__ == "__main__":
    final_matrix, total_rolls = exhaust()
    print(final_matrix)
    print("Total rolls:", total_rolls)

