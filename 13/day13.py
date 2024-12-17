
def read_input():
    with open("input.txt", "r") as file:
        input_string = file.read()

    blocks = input_string.strip().split("\n\n")
    scenarios = []

    for block in blocks:
        lines = block.split("\n")
        
        # values for A
        button_a_values = lines[0].split(":")[1].strip().split(", ")
        x_a = int(button_a_values[0].split("+")[1])
        y_a = int(button_a_values[1].split("+")[1])
        
        #values  B
        button_b_values = lines[1].split(":")[1].strip().split(", ")
        x_b = int(button_b_values[0].split("+")[1])
        y_b = int(button_b_values[1].split("+")[1])
        
        # results
        prize_values = lines[2].split(":")[1].strip().split(", ")
        x_prize = int(prize_values[0].split("=")[1])
        y_prize = int(prize_values[1].split("=")[1])
        
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
    outputs = []
    for a in range(100):
        for b in range(100):
            if ax * a + bx * b == tx and ay * a + by * b == ty:
                outputs.append(3 * a + b)
    if not outputs:
        return 0
    else:
        return min(outputs)

def calc():
    scenarios = read_input()
    total_tokens = sum(solve(scenario) for scenario in scenarios)
    return total_tokens

# Example usage
total_tokens = calc()
print("Total tokens:", total_tokens)
