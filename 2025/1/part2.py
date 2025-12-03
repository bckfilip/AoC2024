
def read_input(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def process_numbers():
    filename = "input.txt"
    lines = read_input(filename)

    start = 50
    zero_count = 0

    for line in lines:
        direction = line[0] 
        clicks = int(line[1:]) 

        movement = -1 if direction == 'L' else 1

        for _ in range(clicks):
            start = (start + movement) % 100 

            if start == 0:
                zero_count += 1 

    return zero_count

if __name__ == "__main__":
    print(process_numbers())
