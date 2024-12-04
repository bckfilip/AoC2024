#--- Day 4: Ceres Search ---

def word_finder():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(row) for row in rows]

    # count XMAS
    count = 0

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == "X":
                # left
                if j > 2:
                    if checkleft(i, j, matrix):
                        count += 1
                # right
                if j < len(row) - 3:
                    if checkright(i, j, matrix):
                        count += 1
                # checkup
                if i > 2:
                    if checkup(i, j, matrix):
                        count += 1
                # down
                if i < len(matrix) - 3:
                    if checkdown(i, j, matrix):
                        count += 1
                # dia up-right
                if j < len(row) - 3 and i > 2:
                    if checkdiaupright(i, j, matrix):
                        count += 1
                # dia up-left
                if j > 2 and i > 2:
                    if checkdiaupleft(i, j, matrix):
                        count += 1
                # dia downright
                if j < len(row) - 3 and i < len(matrix) - 3:
                    if checkdiadownright(i, j, matrix):
                        count += 1
                # dia downleft
                if i < len(matrix) - 3 and j > 2:
                    if checkdiadownleft(i, j, matrix):
                        count += 1
    return count


def checkleft(i, j, matrix):
    return (
        matrix[i][j - 1] == "M" and matrix[i][j - 2] == "A" and matrix[i][j - 3] == "S"
    )


def checkright(i, j, matrix):
    return (
        matrix[i][j + 1] == "M" and matrix[i][j + 2] == "A" and matrix[i][j + 3] == "S"
    )


def checkup(i, j, matrix):
    return (
        matrix[i - 1][j] == "M" and matrix[i - 2][j] == "A" and matrix[i - 3][j] == "S"
    )


def checkdown(i, j, matrix):
    return (
        matrix[i + 1][j] == "M" and matrix[i + 2][j] == "A" and matrix[i + 3][j] == "S"
    )


def checkdiaupright(i, j, matrix):
    return (
        matrix[i - 1][j + 1] == "M"
        and matrix[i - 2][j + 2] == "A"
        and matrix[i - 3][j + 3] == "S"
    )


def checkdiaupleft(i, j, matrix):
    return (
        matrix[i - 1][j - 1] == "M"
        and matrix[i - 2][j - 2] == "A"
        and matrix[i - 3][j - 3] == "S"
    )


def checkdiadownright(i, j, matrix):
    return (
        matrix[i + 1][j + 1] == "M"
        and matrix[i + 2][j + 2] == "A"
        and matrix[i + 3][j + 3] == "S"
    )


def checkdiadownleft(i, j, matrix):
    return (
        matrix[i + 1][j - 1] == "M"
        and matrix[i + 2][j - 2] == "A"
        and matrix[i + 3][j - 3] == "S"
    )


# amount = word_finder()
# print(amount)


### Part 2
def xmas_finder():
    # Read input
    with open("input.txt", "r") as file:
        input_string = file.read()

    rows = input_string.strip().split("\n")
    matrix = [list(row) for row in rows]

    # count XMAS
    count = 0

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == "A" and 0 < i < len(matrix) - 1 and 0 < j < len(row) - 1:
                if xmas_helper(i, j, matrix):
                    count += 1
    return count


def xmas_helper(i, j, matrix):

    if (
        (matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S")
        or (matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M")
    ) and (
        (matrix[i + 1][j - 1] == "M" and matrix[i - 1][j + 1] == "S")
        or (matrix[i + 1][j - 1] == "S" and matrix[i - 1][j + 1] == "M")
    ):
        return True
    return False


count = xmas_finder()
print(count)
