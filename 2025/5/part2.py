def read_input(filename):
    ranges = []

    with open(filename, "r") as file:
        lines = file.readlines()
        split_index = lines.index("\n")

        for line in lines[:split_index]:
            line = line.strip()
            start, end = map(int, line.split("-"))
            new_ranges = []
            
            # start2,end2 is existing values. (1,5)
            # start, end is new line (6,9)
            for start2, end2 in ranges:
                if start <= end2 + 1 and end >= start2 - 1:
                    start = min(start, start2)
                    end = max(end, end2)
                else:
                    new_ranges.append((start2, end2))
            
            new_ranges.append((start, end))
            ranges = new_ranges

    return ranges

def process():
    ranges = read_input("input.txt")
    fresh = 0

    for start, end in ranges:
        fresh += (end + 1) - start

    return fresh, ranges


if __name__ == "__main__":
    fresh, ranges = process()
    print("fresh: ", fresh)
    print("ranges: ", ranges)

