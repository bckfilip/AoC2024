
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()

    lines = input_string.strip().split("\n")
    data = {}
    matrix = []

    # matrix of zeros with the same dimensions as the input
    for line in lines:
        matrix.append([0] * len(line))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isalnum():
                if char not in data:
                    data[char] = []
                data[char].append((y, x))

    return data, matrix

#check if next step is out of bounds
def is_oob(pos, antinodes):
    x, y = pos
    if x < 0 or x >= len(antinodes) or y < 0 or y >= len(antinodes[0]):
        return True
    return False

def has_visited(pos, antinodes):
    x,y = pos
    if antinodes[x][y] == (1):
        return True
    return False

def calculate_positions(current_coord, next_coord):
    x1, y1 = current_coord
    x2, y2 = next_coord
    
    delta_x = x2 - x1
    delta_y = y2 - y1

    pos1 = (x1 - delta_x, y1 - delta_y)  
    pos2 = (x2 + delta_x, y2 + delta_y)  

    return pos1, pos2

def add_antinode(pos, antinodes):
    x, y = pos
    antinodes[x][y] = 1

    return antinodes

def count_unique_antinodes():
    antennas, antinodes = read_input()
    count = 0

    # '0': [(1, 8), (2, 5)
    # char = '0', coordinates = [(1, 8), (2, 5)

    for char, coordinates in antennas.items():
        for i, current_coord in enumerate(coordinates):
            for next_coord in coordinates[i + 1:]:

                pos1, pos2 = calculate_positions(current_coord, next_coord)

                for pos in (pos1, pos2): 
                    if not is_oob(pos, antinodes):
                        if not has_visited(pos, antinodes):
                            antinodes = add_antinode(pos, antinodes)
                            count += 1
    return count

sum = count_unique_antinodes()
print(sum)



