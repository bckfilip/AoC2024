### --- Day 6: Guard Gallivant ---

def read_input():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(row) for row in rows]

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[0 for _ in range(cols)] for _ in range(rows)]

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

def check_next(matrix, pos, direction):
    # Get the next position based on the direction
    next_x, next_y = get_next_position(pos, direction)
    
    # Check if the new position is out of bounds
    if is_oob(matrix, next_x, next_y):
        return 'finished'
    
    # Check the value at the new position
    return 'false' if matrix[next_x][next_y] == '#' else 'true'

def rotate(direction):
    directions = ["up", "right", "down", "left"]
    current_index = directions.index(direction)
    # Rotate 90 degrees right
    new_direction = directions[(current_index + 1) % len(directions)]
    return new_direction

def add_visited(visited, pos, count):
    x, y = pos
    if visited[x][y] == 0:
        visited[x][y] = 1
        count += 1
    return visited, count

def predict_route():
    
    matrix, visited = read_input()
    pos, direction = find_start_pos(matrix)
    count = 0

    while True:
        next_step = check_next(matrix, pos, direction)
        # print(next_step)
        if next_step == 'finished':
            visited, count = add_visited(visited, pos, count)
            break
        elif next_step == 'true':
            visited, count = add_visited(visited, pos, count)
            pos = take_step(pos, direction)
        elif next_step == 'false':
            direction = rotate(direction)
    # print(visited)
    return count



sum = predict_route()
print(sum)