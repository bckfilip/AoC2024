
def parse(data):
    result = []
    index = 0
    i = 0

    while i < len(data):
        # even
        value1 = int(data[i])
        result.append([index] * value1)
        i += 1

        # odd 
        if i < len(data):
            value2 = int(data[i])
            if value2 > 0:
                result.append([-1] * value2)  # -1 as dots
            i += 1

        index += 1

    return result

def move_blocks(parsed_data):

    
    disk_map = [item for sublist in parsed_data for item in sublist]
    
    leftmost_dot_index = 0
    rightmost_index = len(disk_map) - 1

    while leftmost_dot_index < rightmost_index:

        # find left-most dot
        while leftmost_dot_index < len(disk_map) and disk_map[leftmost_dot_index] != -1:
            leftmost_dot_index += 1

        # find the right-most number
        while rightmost_index >= 0 and disk_map[rightmost_index] == -1:
            rightmost_index -= 1

        # swap if good
        if leftmost_dot_index < rightmost_index:
            disk_map[leftmost_dot_index], disk_map[rightmost_index] = disk_map[rightmost_index], -1

            # Move indices inward
            leftmost_dot_index += 1
            rightmost_index -= 1
        else:
            break  

    return disk_map

def calculate_sum(result_list):
    total_sum = 0
    for i, value in enumerate(result_list):
        if value == -1:
            break
        else:
            total_sum += i * value
    return total_sum


def main():
    with open("input.txt", "r") as file:
        input_string = file.read().strip()
    parsed_data = parse(input_string)
    print("Parsed Data:", parsed_data)
    moved_data = move_blocks(parsed_data)  
    print("Moved Data:", moved_data)
    result_sum = calculate_sum(moved_data)
    print("Resulting Sum:", result_sum)

if __name__ == "__main__":
    main()




