# --- Day 2: Red-Nosed Reports ---


# Analyze the unusual data from the engineers. How many reports are safe?

from fileinput import filename


def analyze_reports():
    # Read input
    with open("input.txt", "r") as file:
        data = [list(map(int, line.split())) for line in file]

    correct_reports = 0
    for sublist in data:
        is_increasing = True
        is_decreasing = True
        for i in range(len(sublist) - 1):
            elem = sublist[i]
            next_elem = sublist[i + 1]
            if 1 <= abs(elem - next_elem) <= 3:
                if elem > next_elem:
                    is_increasing = False
                elif elem < next_elem:
                    is_decreasing = False
            else:
                is_increasing = False
                is_decreasing = False
                break
        if is_increasing or is_decreasing:
            correct_reports += 1

    print(correct_reports)


# analyze_reports()

# --- Part Two ---



def analyze_reports():
    # Read input
    with open("input.txt", "r") as file:
        data = [list(map(int, line.split())) for line in file]

    correct_reports = 0

    def is_safe(sublist):
        increasing = all(
            1 <= sublist[i + 1] - sublist[i] <= 3 for i in range(len(sublist) - 1)
        )
        decreasing = all(
            1 <= sublist[i] - sublist[i + 1] <= 3 for i in range(len(sublist) - 1)
        )
        return increasing or decreasing

    for sublist in data:
        if is_safe(sublist):
            correct_reports += 1
        else:
            # remove each level once and check if safe
            for i in range(len(sublist)):
                modified_list = sublist[:i] + sublist[i + 1 :]
                if is_safe(modified_list):
                    correct_reports += 1
                    break

    return correct_reports


num_safe_reports = analyze_reports()
print(f"safe reports: {num_safe_reports}")
