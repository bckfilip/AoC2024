### --- Day 6: Guard Gallivant ---

def read_input():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(row) for row in rows]

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[(0, "") for _ in range(cols)] for _ in range(rows)]

    return matrix, visited

def find_start_pos(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == '^':
                return (i, j), "up"
            elif col == '>':
                return (i, j), "right"
            elif col == 'v':
                return (i, j), "down"
            elif col == '<':
                return (i, j), "left"
    return None

def take_step(pos, direction):
    return get_next_position(pos, direction)

#check if next step is out of bounds
def is_oob(matrix, x, y):

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return True
    return False
    
def get_next_position(pos, direction):
    x, y = pos
    if direction == "up":
        x -= 1
    elif direction == "right":
        y += 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    return x, y

def check_next(matrix, pos, direction, visited):
    next_x, next_y = get_next_position(pos, direction)
    
    if is_oob(matrix, next_x, next_y):
        return 'finished'
    
    if has_visited(visited, pos, direction):
        return 'loop'
    
    return 'false' if matrix[next_x][next_y] == '#' else 'true'

def rotate(direction):
    directions = ["up", "right", "down", "left"]
    current_index = directions.index(direction)
    # Rotate 90 degrees right
    new_direction = directions[(current_index + 1) % len(directions)]
    return new_direction

def add_visited(visited, pos, direction):
    x, y = pos
    if visited[x][y][0] == 0:
        visited[x][y] = (1, direction)
    return visited

def has_visited(visited, pos, direction):
    x,y = pos
    if visited[x][y] == (1, direction):
        return True
    return False


def predict_route(matrix):
    
    _, visited = read_input()
    pos, direction = find_start_pos(matrix)
    loop = False

    while True:
        next_step = check_next(matrix, pos, direction, visited)
        # print(next_step)
        if next_step == 'finished':
            visited = add_visited(visited, pos, direction)
            break
        elif next_step == 'true':
            visited = add_visited(visited, pos, direction)
            pos = take_step(pos, direction)
        elif next_step == 'false':
            direction = rotate(direction)
        elif next_step == 'loop':
            loop = True
            break

    return visited, loop


import copy, time

def main():

    start = time.time()
    original_matrix, _ = read_input()
    start_pos, _ = find_start_pos(original_matrix)
    visited,_ = predict_route(original_matrix)
    success_count = 0

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if (i, j) == start_pos:
                continue

            matrix = copy.deepcopy(original_matrix)
            
            if visited[i][j][0] == 1:
                matrix[i][j] = '#'
                
                _, loop = predict_route(matrix)
                
                if loop:
                    success_count += 1
    end = time.time()
    print("time: ", end - start)
    print("succesful: ", success_count)

main()
