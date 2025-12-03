# --- Day 3: Mull It Over ---


import re


def scanner():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    # match mul(X,Y) x,y = 1-3 digit numbers
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = pattern.findall(input_string)

    sum = 0
    for x, y in matches:
        sum += int(x) * int(y)
    print(sum)
    

# scanner()


# --- Part Two ---



def scanner2():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    pattern = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")

    matches = []
   
    for match in pattern.finditer(input_string):
        if match.group(1): 
            matches.append("do()")
        elif match.group(2):  
            matches.append("don't()")
        elif match.group(3) and match.group(4): 
            matches.append((int(match.group(3)), int(match.group(4))))

    total_sum = 0
    skip = False

    for item in matches:
        if item == "do()":
            skip = False
        elif item == "don't()":
            skip = True
        elif isinstance(item, tuple) and not skip:
            x, y = item
            total_sum += x * y

    print("Total sum:", total_sum)


scanner2()