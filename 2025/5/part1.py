def read_input(filename):
    ranges = []
    my_list = []

    with open(filename, "r") as file:

        lines = file.readlines()
        split_index = lines.index("\n")

        for line in lines[:split_index]:

            line = line.strip()
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
            

        for line in lines[split_index+1:]:
            
            line = line.strip()
            if line:
                number = int(line)
                my_list.append(number)

    return ranges, my_list

def process():
    s, l = read_input("input.txt")
    fresh = 0

    for element in l:
        for start, end in s:
            if start <= element <= end:
                fresh += 1 
                break

    return fresh


if __name__ == "__main__":
    print("Fresh: ", process())

