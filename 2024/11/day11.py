from collections import defaultdict

def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read().strip()
    numbers = map(int, input_string.split())
    numbers_dict = defaultdict(int)
    
    for number in numbers:
        numbers_dict[number] += 1
    
    return dict(numbers_dict)


def split_number(n):
    str_n = str(n)
    midpoint = len(str_n) // 2
    part1 = str_n[:midpoint]
    part2 = str_n[midpoint:]
    num1 = int(part1)
    num2 = int(part2)
    return num1, num2


def blink(numbers_dict, amount):
    count = 0

    while count < amount:
        new_dict = {}

        for key, value in numbers_dict.items():

            # if 0 -> 1
            if key == 0:
                new_key = 1
                
            # if number has even amount of digits -> 2
            elif len(str(key)) % 2 == 0:
                one, two = split_number(key)
                if one in new_dict:
                    new_dict[one] += value
                else:
                    new_dict[one] = value
                if two in new_dict:
                    new_dict[two] += value
                else:
                    new_dict[two] = value
                continue

            else:
                new_key = key * 2024

            if new_key in new_dict:
                new_dict[new_key] += value
            else:
                new_dict[new_key] = value

        numbers_dict = new_dict
        count += 1

    return sum(numbers_dict.values())

def main(amount):
    numbers_dict = read_input()
    print(numbers_dict)
    return blink(numbers_dict, amount)

sum_result = main(75)
print(sum_result)

