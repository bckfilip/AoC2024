def read_input(filename):
    problems = []

    with open(filename, "r") as file:
        lines = file.readlines()

        split_index = None
        for i, line in enumerate(lines):
            if line.strip().startswith("*"):
                split_index = i
                break

        for line in lines[:split_index]:
            nums = line.strip().split()
            for index, num in enumerate(nums):
                if len(problems) <= index:
                    problems.append([])
                problems[index].append(int(num))

        operators = lines[split_index].strip().split()
        for index, op in enumerate(operators):
                problems[index].append(op)

    return problems

def calc():
    problems = read_input("input.txt")
    results = []

    for problem in problems:
        operator = problem[-1] 
        numbers = problem[:-1]
        
        if operator == '+':
            result = sum(numbers)
        else:
            result = 1
            for num in numbers:
                result *= num

        results.append(result)
    
    return results


if __name__ == "__main__":
    results = calc()
    print("sum: ", sum(results))