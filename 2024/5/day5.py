# --- Day 5: Print Queue ---

def parse_input():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    # Split the input into sections
    sections = input_string.strip().split("\n\n")

    # Process the first section
    key_value_pairs = sections[0].strip().split("\n")
    rules = {}
    for pair in key_value_pairs:
        left, right = pair.split("|")
        left = int(left.strip())
        right = int(right.strip())
        if left not in rules:
            rules[left] = []
        rules[left].append(right)

    # Process the second section
    lists = sections[1].strip().split("\n")
    updates = [list(map(int, lst.split(","))) for lst in lists]

    return rules, updates

import math

def findmiddle(list):
    return list[math.floor(len(list)/2)]


def printque():
    rules, updates = parse_input()
    total_sum = 0

    for lst in updates:
        visited = set()
        rule_violation = False 

        for i in lst:
            visited.add(i)
            if i in rules:
                for j in rules[i]:
                    if j in visited:
                        rule_violation = True
                        break
            if rule_violation:
                break  

        if not rule_violation:
            val = findmiddle(lst)
            total_sum += val

    return total_sum

# sum = printque()
# print(sum)



### --- Part 2 ----


def findfaulty():
    rules, updates = parse_input()
    faulty_updates = []

    for lst in updates:
        visited = set()
        rule_violation = False 

        for i in lst:
            visited.add(i)
            if i in rules:
                for j in rules[i]:
                    if j in visited:
                        rule_violation = True
                        break
            if rule_violation:
                faulty_updates.append(lst)
                break 
    return rules, faulty_updates


def fixedque():
    rules, updates = findfaulty()

    total_sum = 0

    for lst in updates:

        while True:
            visited = set()
            rule_violation = False 

            for index, i in enumerate(lst):
                visited.add(i)
                if i in rules:
                    for j in rules[i]:
                        if j in visited:
                            lst.remove(j)
                            lst.insert(index, j)
                            rule_violation = True
                            break
                if rule_violation:
                    break  

            if not rule_violation:
                val = findmiddle(lst)
                total_sum += val
                break

    return total_sum


sum = fixedque()
print(sum)