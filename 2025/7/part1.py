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
    
    for i,row in enumerate(matrix):
        for j,element in enumerate(row):
            if element == "S":
                trace(matrix, i+1, j, visited)
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^" and i > 0 and matrix[i-1][j] == "l":
                count += 1
    
    return matrix, count
                

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
    

if __name__ == "__main__":
    matrix, splits = beams()
    print(f"Splits: ", splits)
    #print(matrix)