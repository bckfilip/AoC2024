
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()

    blocks = input_string.strip().split("\n\n")
    scenarios = []

    for block in blocks:
        lines = block.split("\n")
        
        # values button a
        button_a_values = lines[0].split(":")[1].strip().split(", ")
        x_a = int(button_a_values[0].split("+")[1])
        y_a = int(button_a_values[1].split("+")[1])
        
        #b
        button_b_values = lines[1].split(":")[1].strip().split(", ")
        x_b = int(button_b_values[0].split("+")[1])
        y_b = int(button_b_values[1].split("+")[1])
        
        # result + 10000000000
        prize_values = lines[2].split(":")[1].strip().split(", ")
        x_prize = int(prize_values[0].split("=")[1]) + 10**13
        y_prize = int(prize_values[1].split("=")[1]) + 10**13
        
        scenario = {
            'A': (x_a, y_a),
            'B': (x_b, y_b),
            'Prize': (x_prize, y_prize)
        }
        
        scenarios.append(scenario)
    
    return scenarios

def solve(scenario):
    ax, ay = scenario['A']
    bx, by = scenario['B']
    tx, ty = scenario['Prize']

    # cramers rule 
    
    denominator = (ay * bx) - (by * ax)
    if denominator == 0:
        return 0  

    b = ( (tx * ay) - (ty * ax) ) // denominator
    a = ( (tx * by) - (ty * bx) ) // ( (by * ax) - (bx * ay) )

    if ( (ax * a) + (bx * b) ) == tx and ( (ay * a) + (by * b) ) == ty:
        return 3 * a + b
    else:
        return 0

def calc():
    scenarios = read_input()
    total_tokens = sum(solve(scenario) for scenario in scenarios)
    return total_tokens

total_tokens = calc()
print(" tokens:", total_tokens)
