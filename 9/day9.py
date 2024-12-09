
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()
    return input_string

def parse():
    data = read_input().replace("\n", "")  # Remove newline characters
    new_string = ""

    index = 0
    for i, char in enumerate(data):
        value = int(char)  # Convert the character to an integer
        if i % 2 == 0:
            new_string += str(index) * value
            index += 1
        else:
            new_string += "." * value  # Repeat the dot

    return new_string

def move_blocks():
    disk_map = parse()
    disk_map = list(disk_map)  

    while True:
        # Find the left-most free space
        try:
            leftmost_dot_index = disk_map.index('.')
        except ValueError:
            leftmost_dot_index = len(disk_map)

        # Find the right-most block of numbers
        rightmost_index = len(disk_map) - 1
        while rightmost_index > 0 and disk_map[rightmost_index] == '.':
            rightmost_index -= 1

        # If there are no more blocks to move, break the loop
        if leftmost_dot_index >= rightmost_index:
            break

        # Move one block from the right-most sequence to the left-most dot
        disk_map[leftmost_dot_index] = disk_map[rightmost_index]
        disk_map[rightmost_index] = '.'

    return ''.join(disk_map)

def calculate_sum():
    result_string = move_blocks()
    total_sum = 0
    for i, char in enumerate(result_string):
        if char.isdigit():
            total_sum += i * int(char)
        elif char == '.':
            break  # Stop summing once a dot is encountered
    return total_sum

# Calculate the sum and write it to output2.txt
result_sum = calculate_sum()
with open("output2.txt", "w") as file:
    file.write(str(result_sum))
