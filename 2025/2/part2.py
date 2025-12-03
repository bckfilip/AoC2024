
def parse_ranges(filename):
    ranges = []
    with open(filename, "r") as file:
        input_string = file.read().strip()
    range_strings = input_string.split(',')
    for range_string in range_strings:
        start, end = map(int, range_string.split('-'))
        ranges.append((start, end))
    return ranges

def repeating_patterns(number_str):
    length = len(number_str)
    for i in range(1, length):
        substring = number_str[:i]
        repeat_count = length // i
        if substring * repeat_count == number_str:
            return True
    return False


def invalid_ids():
    ranges = parse_ranges("input.txt")
    invalids = []
    invalidsIncr = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            number_str = str(number)
            if repeating_patterns(number_str):
                invalids.append(number)
                invalidsIncr += int(number)
    return invalids, invalidsIncr

if __name__ == "__main__":
    print(invalid_ids())
