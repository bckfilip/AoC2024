def read_input(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            digits = [char for char in line if char.isdigit()]
            numbers.append(digits)

    return numbers

def high_joltage():
    batteries = read_input("input.txt")
    tot_values = []
    
    for digits in batteries:
        result = []
        start = 0
        
        for pos in range(12):
            end = len(digits) - (12 - pos) + 1 
            best_digit = max(digits[start:end])
            best_index = digits.index(best_digit, start)
            result.append(best_digit)
            start = best_index + 1
        
        largest_number = ''.join(result)
        tot_values.append(largest_number)

    total_sum = sum(int(value) for value in tot_values)
    return tot_values, total_sum
            
if __name__ == "__main__":
    print(high_joltage())
