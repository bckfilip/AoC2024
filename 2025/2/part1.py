
def parse_ranges(filename):
    ranges = []
    with open(filename, "r") as file:
        input_string = file.read().strip()
    range_strings = input_string.split(',')
    for range_string in range_strings:
        start, end = map(int, range_string.split('-'))
        ranges.append((start, end))
    return ranges

def invalid_ids():
    ranges = parse_ranges("input.txt")
    invalids = []
    invalidsIncr = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            number_str = str(number)
            length = len(number_str)
            if length % 2 != 0:
                continue
            half_length = length // 2
            first_half = number_str[:half_length]
            second_half = number_str[half_length:]
            if first_half == second_half:
                invalids.append(number)
                invalidsIncr += int(number)
    return invalids, invalidsIncr

if __name__ == "__main__":
    print(invalid_ids())
