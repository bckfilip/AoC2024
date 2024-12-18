
from collections import defaultdict

def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()
    rows = input_string.strip().split("\n")
    guards = defaultdict(list)

    for row in rows:
        parts = row.split(" ")
        p_values = parts[0].split("=")[1].split(",")
        v_values = parts[1].split("=")[1].split(",")

        p = (int(p_values[0]), int(p_values[1]))
        v = (int(v_values[0]), int(v_values[1]))

        guards[p].append(v)

    return dict(guards)

def write_map_to_file(guards, iteration, file):
    
    map_ = [["-"] * 103 for _ in range(101)]

    for position in guards:
        map_[position[0]][position[1]] = "X"

    file.write(f"Iteration {iteration}:\n")
    for row in map_:
        file.write(''.join(map(str, row)) + "\n")
    file.write("\n")

def move(guards, iterations):
    with open("output.txt", "w") as file:
        for i in range(iterations):
            new_guards = defaultdict(list)
            for position in guards:
                for velocity in guards[position]:
                    new_x = (position[0] + velocity[0]) % 101
                    new_y = (position[1] + velocity[1]) % 103
                    new_guards[new_x, new_y].append(velocity)
            guards = new_guards

            # Write the map every 10 iterations
            ## FOUND IT :D 
            if i == 6875:
                write_map_to_file(guards, i, file)

    return guards

def main():
    guards = read_input()
    guards = move(guards, 10000)
    x1 = x2 = x3 = x4 = 0

    for position in guards:
        if position[0] == 50 or position[1] == 51:
            continue

        # first quad
        if position[0] < 50 and position[1] < 51:
            x1 += len(guards[position])

        # second quad
        if position[0] > 50 and position[1] < 51:
            x2 += len(guards[position])

        # third quad
        if position[0] < 50 and position[1] > 51:
            x3 += len(guards[position])

        # fourth quad
        if position[0] > 50 and position[1] > 51:
            x4 += len(guards[position])

    print(f"x1: {x1}, x2: {x2}, x3: {x3}, x4: {x4}")
    summa = x1 * x2 * x3 * x4
    print(summa)
    #print(guards)
    return summa

main()
