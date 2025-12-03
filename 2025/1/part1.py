
def read_input(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("L"):
                numbers.append(-int(line[1:]))
            else:
                numbers.append(int(line[1:]))

    return numbers

def process_numbers():
    filename = "input.txt"
    numbers = read_input(filename)

    start = 50
    inc = 0
    for num in numbers:
        start += num
        if start % 100 == 0:
            inc += 1

    return inc

if __name__ == "__main__":
    print(process_numbers())
