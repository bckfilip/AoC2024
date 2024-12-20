
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()

    lines = input_string.strip().split("\n")
    data = []

    for line in lines:
        key, values = line.split(":")
        key = int(key.strip())
        values_list = list(map(int, values.strip().split()))
        data.append((key, values_list))

    return data


from itertools import product


def create_operation_matrix(size):
    operations = ["+", "*", "||"]

    combinations = list(product(operations, repeat=size))
    matrix = [list(combination) for combination in combinations]
    return matrix


def calibrate(values, combinations, key):
    for combination in combinations:
        result = values[0]
        for i, operation in enumerate(combination):
            if operation == "+":
                result += values[i + 1]
            elif operation == "*":
                result *= values[i + 1]
            elif operation == "||":
                concat = str(result) + str(values[i + 1])
                result = int(concat)
        if result == key:
            return True

    return False


def count_calibration():
    data = read_input()
    count = 0
    total_sum = 0

    for key, value_list in data:
        combinations = create_operation_matrix(len(value_list) - 1)
        if calibrate(value_list, combinations, key):
            count += 1
            total_sum += key
            # print(f"success Key: {key}, Values: {value_list}")

    return count, total_sum


count, total_sum = count_calibration()
print("Count: ", count, "Sum: ", total_sum)
