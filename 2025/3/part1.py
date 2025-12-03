def read_input(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            numbers.append(line)

    return numbers

def high_joltage():
    batteries = read_input("input.txt")
    values = []
    total = 0
    
    for b in batteries:
        firstValue = 0
        first_index = 0
        
        for i in range(len(b) - 1):
            digit_val = int(b[i])
            if digit_val > firstValue:
                firstValue = digit_val
                first_index = i
        
        secondValue = 0
        for i in range(first_index + 1, len(b)):
            digit_val = int(b[i])
            if digit_val > secondValue:
                secondValue = digit_val
        final = str(firstValue) + str(secondValue)
        total += int(final)
        values.append(final)
    
    return values, total
            


if __name__ == "__main__":
    print(high_joltage())
