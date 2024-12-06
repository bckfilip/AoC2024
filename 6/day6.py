### --- Day 6: Guard Gallivant ---

def predict_route():
        # Read input
    with open("exinput.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(row) for row in rows]

    print(matrix)







predict_route()