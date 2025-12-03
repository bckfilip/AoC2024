
# --- Day 1: Historian Hysteria ---


# read input and convert data to lists
from collections import Counter


def read_file(filename):
    left = []
    right = []
    with open(filename, "r") as file:
        for line in file:
            # Split each line into two parts and convert them to integers
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))

    return left, right


def calc_dist():
    left, right = read_file("input.txt")
    left.sort()
    right.sort()
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    print(distance)


# calc_dist()

## --- Part Two ---



def calc_similarity():
    left, right = read_file("input.txt")
    rightCounter = Counter(right)
    similarity = 0
    for i in range(len(left)):
        if left[i] in rightCounter:
            similarity += left[i] * rightCounter[left[i]]
    print(similarity)


calc_similarity()
